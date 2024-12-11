#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/10 14:39
# @Author  : MrLiu
# @File    : 6斐波那契数列.py
# @Description : 斐波那契数列.
# n 个数.
def func(num):
    if num <= 2:
        return 1
    a = 1
    b = 1
    for i in range(num - 2):
        a, b = b, a + b
    return b

def fib(n):
    return 1 if n<=2 else fib(n - 2)+fib(n - 1)

if __name__ == "__main__":
    while True:
        num = int(input("num: "))
        if func(num) == fib(num):
            print("True")
        else:
            print("False")

