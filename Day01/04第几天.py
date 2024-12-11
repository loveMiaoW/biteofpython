#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/7 12:35
# @Author  : MrLiu
# @File    : 04第几天.py
# @Description : 输入年月日,判断这一天是这年的第几天.

def isLeepYear(argc):
    if argc % 400 == 0 or (argc % 4 == 0 and argc % 100 != 0):
        return True
    else:
        return False

def func():
    ret = 0
    yue_obj = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    year = int(input("input year: "))
    yue = int(input("input yue: "))
    day = int(input("input day: "))
    if isLeepYear(year):
        yue_obj[2] += 1

    for i in range(yue):
        ret += yue_obj[i]
    ret += day
    print(ret)


if __name__ == "__main__":
    func()
