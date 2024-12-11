#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/10 14:51
# @Author  : MrLiu
# @File    : 07九九乘法表.py
# @Description :

def func():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%d * %d = %2ld '%(j,i,i*j),end="")
        print()

if __name__ == "__main__":
    func()
