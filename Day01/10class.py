#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/11 10:12
# @Author  : MrLiu
# @File    : 10class.py
# @Description : object.
# Coding = UTF-8
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __say_hi(self):
        print("Person's name is {},say_hi.".format(self.name))
    def use_say_hi(self):
        self.__say_hi()

class Robot:
    # 类变量 对象变量
    population = 0
    num = 0
    def __init__(self,name):
        self.name = name
        print("Init {}.".format(self.name))
        Robot.population += 1
        self.num += 1

    def die(self):
        print("{} is die.".format(self.name))
        Robot.population -= 1
        self.num -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("now has {} / {} robots working.".format(self.population,self.num))

    #staticmethod
    @classmethod
    def how_many(cls):
        print("we have {} / {} robots.".format(cls.population,cls.num))



# BASE CLASS
class SchoolMerber:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("(Init School Merber {}.)".format(self.name))

    def tell(self):
        print("Name:{}, Age:{}.".format(self.name,self.age),end=" ")


# DERIVED CLASS
class Teacher(SchoolMerber):
    def __init__(self,name,age,salary):
        SchoolMerber.__init__(self,name,age)
        self.salary = salary
        print("Init Teacher{}.".format(self.name))

    def tell(self):
        SchoolMerber.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMerber):
    '''代表一位学生。'''
    def __init__(self, name, age, marks):
        SchoolMerber.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))
    def tell(self):
        SchoolMerber.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


def func():

    t = Teacher('love',40,100000)
    s = Student('Swaroop', 25, 75)
    members = [t, s]
    for member in members:
        # 对全体师生工作
        member.tell()



if __name__ == "__main__":
    func()
