import os
import sys
import subprocess


# Переименовывает все apk файлы в каталоге по маске - application-label_PACKAGENAME_versionCODE_versionNAME.apk
# В переменной PATH должен быть путь до aapt2 или в папке запуска скрипта лежать сам aapt2. Взять из  AndroidSDK. Buildtools

# aapt2 dump badging phyphox_v1.1.3_apkpure.com.apk


def getMeNewName(s):
    cmd = f'aapt2 dump badging  {s}'
    subprocess.call(cmd, stderr=None, stdout=None, shell=True)
    pass


def main():
    os.chdir(os.path.abspath(os.path.curdir))
    file = os.path.curdir
    strings = os.listdir(file)
    s = ""
    name = ""
    new_name = ""
    for s in strings:
        print(s)
        print(os.path.isfile(os.path.normpath(s)))
        if os.path.isfile(s) and s.rpartition(".")[2] == "apk":
            new_name = getMeNewName(s)
            os.rename(s, new_name)

    print("Готов: " + s)
    pass


if __name__ == '__main__':
    main()
