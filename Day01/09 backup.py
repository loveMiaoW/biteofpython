#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/10 15:25
# @Author  : MrLiu
# @File    : 09 backup.py
# @Description : start cmd
# 做什么   What
# 怎么做   How
# 开始做   Do it
# 测试    Test
# 使用    Use
# 维护    Maintain
import os
import time

def func():
    source_path = str('C:/Users/kikuru/Desktop/pythonProject/1/')
    target_path = str("C:/Users/kikuru/Desktop/pythonProject/backup")

    target = target_path + os.sep + time.strftime("%Y%m%d%H%M%S") + ".zip"

    if not os.path.exists(target_path):
        os.mkdir(target_path)

    zip_comm = 'zip -r {0} {1}'.format(target, source_path)
    print(source_path)
    print("Zip command is: ")
    print(zip_comm)
    print('Runing...')

    if os.system(zip_comm) == 0:
        print('Successful backup to ', target)
    else:
        os.system("start cmd")
        print("Backup false")


if __name__ == "__main__":
    func()
