#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/7 12:04
# @Author  : MrLiu
# @File    : 03完全平方数.py
# @Description : 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 168在两个平方数之间差距微乎其微
# 可以先找到根数
# 从1遍历到根数平方
# 检验i+100 和 i + 168
import math


def func():
    n = 0
    while (n + 1)**2 - n**2 <= 168:
        n += 1
    for i in range((n + 1) ** 2):
       flag = (i + 100) == int(math.sqrt(i + 100)) ** 2
       flag01 = (i + 168) == int(math.sqrt(i + 168)) ** 2
       if flag and flag01:
            if i - 100 >= 0:
                print(i - 100)
if __name__ == "__main__":
    func()