import os
import sys
import subprocess


# TODO
# Несколько потоков на распаковку

def main():
    os.chdir(os.path.abspath(os.path.curdir))
    file = os.path.curdir
    strings = os.listdir(file)

    s = ""
    for s in strings:

        print(s)
        print(os.path.isfile(os.path.normpath(s)))
        if os.path.isfile(s) and s.rpartition(".")[2] == "apk":
            cmd = f"apktool d -b {os.path.normpath(s)}"
            subprocess.call(cmd, stderr=None, stdout=None, shell=True)
    print("Готов: " + s)
    pass


if __name__ == '__main__':
    main()
