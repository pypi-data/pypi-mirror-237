import psutil
import socket
import subprocess


def get_result_dict_from_set(all_set, task_dict):
    print("all_set length=", len(all_set))
    result_dict = {}
    for item in all_set:
        found = False  # 标记是否找到匹配的任务
        for task in task_dict.keys():
            if task in item:
                result_dict[task] = True
                found = True
                break  # 只跳出当前的内部循环
        if found:
            continue  # 继续下一个外部循环
    return result_dict


def find_all_process():
    all_set = set()
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            proc_info = proc.as_dict(attrs=['pid', 'name'])
            process_name = proc_info['name'].lower()
            all_set.add(process_name)
            print("+", end="", flush=True)
            child_procs = psutil.Process(proc_info['pid']).children(recursive=True)
            for child_proc in child_procs:
                child_proc_info = child_proc.as_dict(attrs=['pid', 'name'])
                child_process_name = child_proc_info['name'].lower()
                all_set.add(child_process_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return all_set


def check_processes(task_dict):
    print("enter check_processes, try to find name in all process and child process")

    all_set = find_all_process()
    result_dict = get_result_dict_from_set(all_set, task_dict)
    print("result_dict", result_dict)
    false_keys = [key for key in task_dict.keys() if key not in result_dict.keys()]
    print("false_keys", false_keys)
    if false_keys:
        print(" 和 ".join(false_keys) + "未运行", "请及时检查")
    return false_keys


def check_port_in_use(port):
    # 检查指定端口是否被占用
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('localhost', port))
        except OSError:
            print("# 端口被占用，查找占用端口的进程")
            for conn in psutil.net_connections():
                if conn.status == "LISTEN" and conn.laddr.port == port:
                    pid = conn.pid
                    process = psutil.Process(pid)
                    print(f"# 占用端口的进程名：{process.name()}，进程路径：{process.exe()}")
                    return process.name(), process.exe()
    return None, None


def terminate_process_using_port(port):
    try:
        command = f"netstat -ano | findstr :{port}"
        output = subprocess.check_output(command, shell=True, text=True)
        lines = output.strip().split("\n")
        for line in lines:
            parts = line.split()
            pid = int(parts[-1])
            subprocess.run(["taskkill", "/F", "/PID", str(pid)])
        print("已结束占用该端口的程序")
        return pid
    except (subprocess.CalledProcessError, ValueError) as e:
        print(f"结束占用该端口的程序时出现错误：{e}")
        return None


if __name__ == '__main__':

    print(check_port_in_use(3306))

    exit()
    task_dict = {'jiepan': 'D:/Soft/_lyytools/_jiepan/_jiepan.exe', 'gui-only': 'D:/Soft/_lyytools/gui-only/gui-only.exe', 'kingtrader': 'D:/Soft/_Stock/KTPro/A.点我登录.exe'}
    stopped = check_processes(task_dict)
    print("stopped=", stopped)
