import sys
import subprocess

def call_proc_getout(cmd_list):
    proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        err = proc.stderr.readline()
        print(err)
        if err != "":
            print('stderr : ' + err)
        if line != "":
            print("yield")
            yield line
        else:
            break
    """
    for line in iter(proc.stdout.readline, ""):
        print(line)
        yield line
    """
    while True:
        if proc.poll() is not None:
            break


def main():
    cmd = [sys.executable, 'child.py']
    for out in call_proc_getout(cmd):
        print('coller : ' + out)

if __name__ == "__main__":
    main()

