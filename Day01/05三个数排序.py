#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/10 14:34
# @Author  : MrLiu
# @File    : 05三个数排序.py
# @Description : 三个数排序.
# 只考虑整型
# 可扩展至浮点型,小数,复数.
def func():
    a = []
    for i in range(3):
        num = int(input("num: "))
        a.append(num)
    a.sort()
    print(a)

if __name__ == "__main__":
    func()
