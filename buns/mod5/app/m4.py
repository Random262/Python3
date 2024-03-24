import sys


class Redirect:
    def __init__(self, stdout=None, stderr=None):
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr
        self.stdout = stdout
        self.stderr = stderr

    def __enter__(self):
        if self.stdout:
            sys.stdout = self.stdout
        if self.stderr:
            sys.stderr = self.stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
            sys.stdout = self.old_stdout
            sys.stderr = self.old_stderr


if __name__ == "__main__":
    print('Hello stdout')
    stdout_file = open('stdout.txt', 'w')
    stderr_file = open('stderr.txt', 'w')

    with Redirect(stdout=stdout_file, stderr=stderr_file):
        print('Hello stdout.txt')
        raise Exception('Hello stderr.txt')
    stdout_file.close()
    stderr_file.close()

