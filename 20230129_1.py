######################################
# 4-1. 图文 - if 条件判断【https://crossincode.com/school/lesson/196/】
"""
print("◆age: ", end="")
age = int(input())
if age >= 18:
    print("你是个成年人了！")
"""
import random

######################################
"""
num = 10
print('◆Guess what I think?')
answer = int(input())
if answer < num:
    print('too small!')
if answer > num:
    print('too big!')
if answer == num:
    print('BINGO!')
"""
######################################

"""
num = 111
print("◆Guess what I think?")
answer = int(input("Please input a number: "))
if answer < num:
    print("too small!")
elif answer > num:
    print("too big!")
else:
    print("BING GO!!")
"""

######################################

# 4-4. 图文 - while 循环【https://crossincode.com/school/lesson/197/】

"""
num = 123
print("◆Guess what I think?")
answer = int(input("Please input a number: "))
while answer != num:
    if answer < num:
        print("too small!")
        answer = int(input("Please input a number: "))
    else:   #这里answer的值有可能大于num，也有可能等于num。但是用不能加判断式的else也实现了elif同样的结果。使用else时，answer==num的情况由while进行了判断。
        print("too big!")
        answer = int(input("Please input a number: "))
print("BING GO!!")
"""
"""
num = 123
print("◆Guess what I think?")
answer = False
while answer != num:
    answer = int(input("Please input a number: "))
    if answer < num:
        print("too small!")
    elif answer > num:
        print("too big!")
print("BING GO!!")
"""

######################################
#　 4-7. 图文 - for 循环【https://crossincode.com/school/lesson/198/】
"""
i = 0
while i < 5:
    i += 1
    for j in range(3):
        print(j)
        if j == 2:
            break
    for k in range(3):
        if k == 2:
            continue
        print(k)
    if i > 3:
        break
    print(i)
"""
########################
#自动生成10个IP地址
octet_1_2_3 = "192.168.10."
for octet_4 in range(1, 11):
    print(octet_1_2_3 + str(octet_4))

