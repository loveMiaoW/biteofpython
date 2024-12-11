import os
import sys


while False:
    print("1")
    if int(input("1")) == 1:
        break
else:
    print("2")


with open("1.txt","r") as f:
    for line in f:
        print(line.strip())


my_list = [1,2,2,3,4,3]
un_list = list(set(my_list))
print(un_list)


def count_greater_than_ten(objs):
    num = 0
    for x in objs:
        if x > 10:
            num = num + 1
    print(f"大于10的数字有{num}个")

count_greater_than_ten([15,22,9,3,17])

def swap(a,b):
    a,b = b,a
    print(f"a={a},b={b}")

swap("hello","world")


students={
    "1":{"age":2,"university":"3","major":"4"},
    "11":{"age":22,"university":"33","major":"44"},
}

while True:
    print("1 input/2 all/0 quit")
    choise = int(input("input choise: "))
    if choise == 0:
        break
    elif choise == 1:
        name = input("input name: ")
        if name in students:
            print("姓名存在,更新信息.")
            age = int(input("input age: "))
            university = input("input university: ")
            major = input("input major: ")
            students[name]["age"] = age
            students[name]["university"] = university
            students[name]["major"] = major
            print("更新成功.")
        else:
            print("输入信息.")
            age = int(input("input age: "))
            university = input("input university: ")
            major = input("input major: ")
            students[name] = {"age": age, "university": university, "major": major}
            print("插入成功.")
    elif choise == 2:
        for name, info in students.items():
            print(name, info["age"], info["university"], info["major"])






