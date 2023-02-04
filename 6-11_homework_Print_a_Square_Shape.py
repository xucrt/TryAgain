######################################
#6-11. 编程实例 - 打印图形
#https://crossincode.com/school/lesson/89/

def square(a=5, b=5, c="*"):
    for i in range(0, int(a)):
        for o in range(0, int(b)):
            print(c, end=" ")
        print()


square()
count = 0
while count < 2:
    count += 1
    square(input("请输入矩形的高： "), input("请输入矩形的宽： "), input("请输入构成矩形的符号： "))
