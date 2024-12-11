#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/6 19:21
# @Author  : MrLiu
# @File    : 01组合数.py.py
# @Description : 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

def func():
    num = 0
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if ((i != j) and (i != k) and (j != k)):
                    print(i,j,k)
                    num += 1
    print(num)

if __name__ == "__main__":
    func()