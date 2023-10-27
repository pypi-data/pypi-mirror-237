from toolbox import get_log_folder, update_ui, gen_time_str, trimmed_format_exc, promote_file_to_downloadzone
import time, os

class PipeCom():
    def __init__(self, cmd, content) -> None:
        self.cmd = cmd
        self.content = content


class PluginMultiprocessManager():
    def __init__(self, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
        # ⭐ 主进程
        self.autogen_work_dir = os.path.join(get_log_folder('autogen'), gen_time_str())
        self.previous_work_dir_files = {}
        self.llm_kwargs = llm_kwargs
        self.plugin_kwargs = plugin_kwargs
        self.chatbot = chatbot
        self.history = history
        self.system_prompt = system_prompt
        self.web_port = web_port
        self.alive = True

    def is_alive(self):
        return self.alive

    def launch_subprocess_with_pipe(self):
        # ⭐ 主进程
        from multiprocessing import Process, Pipe
        parent_conn, child_conn = Pipe()
        self.p = Process(target=self.subprocess_worker, args=(child_conn,))
        self.p.daemon = True
        self.p.start()
        return parent_conn

    def terminate(self):
        self.p.terminate()
        self.alive = False
        print('[debug] instance terminated')

    def subprocess_worker(self, child_conn):
        # ⭐⭐ 子进程
        raise NotImplementedError

    def send_command(self, cmd):
        # ⭐ 主进程
        self.parent_conn.send(PipeCom("user_input", cmd))

    def immediate_showoff_when_possible(self, fp):
        # ⭐ 主进程
        # 获取fp的拓展名
        file_type = fp.split('.')[-1]
        # 如果是文本文件, 则直接显示文本内容
        if file_type in ['png', 'jpg']:
            image_path = os.path.abspath(fp)
            self.chatbot.append(['检测到新生图像:', f'本地文件预览: <br/><div align="center"><img src="file={image_path}"></div>'])
            yield from update_ui(chatbot=self.chatbot, history=self.history)

    def overwatch_workdir_file_change(self):
        # ⭐ 主进程 Docker 外挂文件夹监控
        path_to_overwatch = self.autogen_work_dir
        change_list = []
        # 扫描路径下的所有文件, 并与self.previous_work_dir_files中所记录的文件进行对比，
        # 如果有新文件出现，或者文件的修改时间发生变化，则更新self.previous_work_dir_files中
        # 把新文件和发生变化的文件的路径记录到 change_list 中
        for root, dirs, files in os.walk(path_to_overwatch):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path not in self.previous_work_dir_files.keys():
                    last_modified_time = os.stat(file_path).st_mtime
                    self.previous_work_dir_files.update({file_path:last_modified_time})
                    change_list.append(file_path)
                else:
                    last_modified_time = os.stat(file_path).st_mtime
                    if last_modified_time != self.previous_work_dir_files[file_path]:
                        self.previous_work_dir_files[file_path] = last_modified_time
                        change_list.append(file_path)
        if len(change_list) > 0:
            file_links = ''
            for f in change_list: 
                res = promote_file_to_downloadzone(f)
                file_links += f'<br/><a href="file={res}" target="_blank">{res}</a>'
                yield from self.immediate_showoff_when_possible(file_path)

            self.chatbot.append(['检测到新生文档.', f'文档清单如下: {file_links}'])
            yield from update_ui(chatbot=self.chatbot, history=self.history)
        return change_list


    def main_process_ui_control(self, txt, create_or_resume) -> str:
        # ⭐ 主进程
        if create_or_resume == 'create':
            self.cnt = 1
            self.parent_conn = self.launch_subprocess_with_pipe() # ⭐⭐⭐
        self.send_command(txt)
        if txt == 'exit': 
            self.chatbot.append([f"结束", "结束信号已明确，终止AutoGen程序。"])
            yield from update_ui(chatbot=self.chatbot, history=self.history)
            self.terminate()
            return "terminate"
        
        while True:
            time.sleep(0.5)
            if self.parent_conn.poll(): 
                if '[GPT-Academic] 等待中' in self.chatbot[-1][-1]:
                    self.chatbot.pop(-1)    # remove the last line
                msg = self.parent_conn.recv() # PipeCom
                if msg.cmd == "done":
                    self.chatbot.append([f"结束", msg.content]); self.cnt += 1
                    yield from update_ui(chatbot=self.chatbot, history=self.history)
                    self.terminate(); break
                if msg.cmd == "show":
                    yield from self.overwatch_workdir_file_change()
                    self.chatbot.append([f"运行阶段-{self.cnt}", msg.content]); self.cnt += 1
                    yield from update_ui(chatbot=self.chatbot, history=self.history)
                if msg.cmd == "interact":
                    yield from self.overwatch_workdir_file_change()
                    self.chatbot.append([f"程序抵达用户反馈节点.", msg.content + 
                                         "\n\n等待您的进一步指令." + 
                                         "\n\n(1) 一般情况下您不需要说什么, 清空输入区, 然后直接点击“提交”以继续. " +
                                         "\n\n(2) 如果您需要补充些什么, 输入要反馈的内容, 直接点击“提交”以继续. " +
                                         "\n\n(3) 如果您想终止程序, 输入exit, 直接点击“提交”以终止AutoGen并解锁. "
                    ])
                    yield from update_ui(chatbot=self.chatbot, history=self.history)
                    # do not terminate here, leave the subprocess_worker instance alive
                    return "wait_feedback"
            else:
                if '[GPT-Academic] 等待中' not in self.chatbot[-1][-1]:
                    self.chatbot.append(["[GPT-Academic] 等待AutoGen执行结果 ...", "[GPT-Academic] 等待中"])
                self.chatbot[-1] = [self.chatbot[-1][0], self.chatbot[-1][1].replace("[GPT-Academic] 等待中", "[GPT-Academic] 等待中.")]
                yield from update_ui(chatbot=self.chatbot, history=self.history)

        self.terminate()
        return "terminate"

    def subprocess_worker_wait_user_feedback(self, wait_msg="wait user feedback"):
        # ⭐⭐ 子进程
        patience = 5 * 60
        begin_waiting_time = time.time()
        self.child_conn.send(PipeCom("interact", wait_msg))
        while True:
            time.sleep(0.5)
            if self.child_conn.poll(): 
                wait_success = True
                break
            if time.time() - begin_waiting_time > patience:
                self.child_conn.send(PipeCom("done", ""))
                wait_success = False
                break
        return wait_success

