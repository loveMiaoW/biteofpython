#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/6 22:18
# @Author  : MrLiu
# @File    : 02个税计算.py.py
# @Description : 个税计算.

# 给出两种解法
#100000 200000 400000 600000 1000000 +
#0.1    0.075  0.05   0.03    0.015  0.01
#240 230
#
def func(agrc):
    ret = 0
    num = agrc

    if num <= 100000:
        ret += num * 0.1
    elif num > 100000 and num < 200000:
        ret += (100000 * 0.1 + (num - 100000) * 0.075)
    elif num >= 200000 and num < 400000:
        ret += (100000 * 0.1 + 100000 * 0.075 + (num - 200000) * 0.05)
    elif num >= 400000 and num < 600000:
        ret += (100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (num - 400000) * 0.03)
    elif num >= 600000 and num < 1000000:
        ret += (10000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (num - 600000) * 0.015)
    else:
        ret += 10000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (num - 1000000) * 0.01
    return ret


def func01(argc):
    ret = 0

    th = [100000,200000,400000,600000,1000000]
    rates = [0.1,0.075,0.05,0.03,0.015,0.01]

    num = argc

    for i in range(len(th)):
        if num <= th[i]:
            ret += num * rates[i]
            num = 0
            break;
        else:
            if i == 0:
                ret += th[i] * rates[i]
                num -= th[i]
            else:
                ret += (th[i] - th[i - 1]) * rates[i]
                num -= (th[i] - th[i - 1])
    ret += num * rates[-1]
    return ret


if __name__ == "__main__":
    while True:
        num = int(input("input num: "))
        if func(num) == func01(num):
            print("Ture")
        else:
            print("False")
