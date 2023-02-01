######################################
# 4-15. 编程实例 - BMI 指数测试
# https://crossincode.com/school/lesson/77/

# ［Python入門］Pythonの演算子まとめ
# https://atmarkit.itmedia.co.jp/ait/articles/1907/23/news010.html

"""
w = input("请输入体重(公斤)： ")
h = input("请输入身高(米)： ")

BMI = float(w) / (float(h) ** 2)

if BMI < 18.5:
    print("您的BMI为%.2f,您体重偏轻。" % BMI)
elif 18.5 <= BMI < 24:
    print("您的BMI为%.2f,您体重正常。" % BMI)
elif BMI >= 24:
    print("您的BMI为%.2f,您是一头肥猪!" % BMI)

#https://gitee.com/crossin/crossincode/blob/master/bmi/bmi.py
# python3.5
#分别输入身高与体重
height = float(input('输入你的身高(米):'))
weight = float(input('输入你的体重(公斤):'))
#算出bmi指数
bmi = weight / (height * height)
#判断并输出
print('BMI:%.2f' % bmi)
if bmi < 18.5:
    print('体重偏轻')
elif bmi >= 24:
    print('体重偏重')
else:
    print('体重正常')
"""

######################################
# 5-7. 编程实例 - 猜数字
# https://crossincode.com/school/lesson/73/

import random

answer = False
count = 0
i = 1

while not answer:
    print("◆Guess what I think?\n \
    This is round %d.\n \
    You have %d BINGO now!" % (i, count))
    num = random.randint(1, 9)
    while answer != num:
        answer = int(input("Please input a number: "))
        if answer < num:
            print("too small!")
        elif answer > num:
            print("too big!")
        else:
            i += 1
            count += 1
            print("BING GO!!")
            answer = False
            break

