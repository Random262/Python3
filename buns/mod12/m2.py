import subprocess
import getpass


def process_count(username: str) -> int:
    command = f"ps -u {username} | wc -l"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return int(result.stdout.strip()) - 1
    else:
        print("ps command error")
        return -1


def total_memory_usage(root_pid: int) -> float:
    command = f"ps -o %mem --ppid {root_pid} --no-headers | awk '{{sum+=$1}}END{{print sum}}'"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return float(result.stdout.strip())
    else:
        print("ps command error")
        return -1


if __name__ == "__main__":
    username = getpass.getuser()
    root_pid = 1
    print(f"Number of processes of the current user: {process_count(username)}")
    print(f"Total memory consumption of the process tree with root {root_pid}: {total_memory_usage(root_pid)}%")