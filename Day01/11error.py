#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/11 14:52
# @Author  : MrLiu
# @File    : 11error.py
# @Description : 异常.

class ShortInputException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

def func():
    try:
        text = input()

        if len(text) < 3:
            raise ShortInputException(len(text),3)
    except EOFError:
        print("EOF")
    except ShortInputException as ex:
        print("ShortInputException: The input was {0} long,expected at least {1}".format(ex.length,ex.atleast))
    else:
        print("No exception raise.")



if __name__ == "__main__":
    func()
