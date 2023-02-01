"""
import random

num = random.randint(1, 999)
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
# https://crossincode.com/school/lesson/46/
"""
for i in range(1, 10):
    for j in range(i, 10):
        r = i * j
        print('%d x %d = %.2d' % (i, j, r), end="  ")
        if j == 9:
            break
    print()

生成结果：
1 x 1 = 01  1 x 2 = 02  1 x 3 = 03  1 x 4 = 04  1 x 5 = 05  1 x 6 = 06  1 x 7 = 07  1 x 8 = 08  1 x 9 = 09  
2 x 2 = 04  2 x 3 = 06  2 x 4 = 08  2 x 5 = 10  2 x 6 = 12  2 x 7 = 14  2 x 8 = 16  2 x 9 = 18  
3 x 3 = 09  3 x 4 = 12  3 x 5 = 15  3 x 6 = 18  3 x 7 = 21  3 x 8 = 24  3 x 9 = 27  
4 x 4 = 16  4 x 5 = 20  4 x 6 = 24  4 x 7 = 28  4 x 8 = 32  4 x 9 = 36  
5 x 5 = 25  5 x 6 = 30  5 x 7 = 35  5 x 8 = 40  5 x 9 = 45  
6 x 6 = 36  6 x 7 = 42  6 x 8 = 48  6 x 9 = 54  
7 x 7 = 49  7 x 8 = 56  7 x 9 = 63  
8 x 8 = 64  8 x 9 = 72  
9 x 9 = 81  
"""

######################################
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d x %d = %d' % (i, j, i*j), end="  ")
        if i == j:
            print()
#【%.2d】　输出结果：1 x 1 = 01

输出结果：
1 x 1 = 1  
2 x 1 = 2  2 x 2 = 4  
3 x 1 = 3  3 x 2 = 6  3 x 3 = 9  
4 x 1 = 4  4 x 2 = 8  4 x 3 = 12  4 x 4 = 16  
5 x 1 = 5  5 x 2 = 10  5 x 3 = 15  5 x 4 = 20  5 x 5 = 25  
6 x 1 = 6  6 x 2 = 12  6 x 3 = 18  6 x 4 = 24  6 x 5 = 30  6 x 6 = 36  
7 x 1 = 7  7 x 2 = 14  7 x 3 = 21  7 x 4 = 28  7 x 5 = 35  7 x 6 = 42  7 x 7 = 49  
8 x 1 = 8  8 x 2 = 16  8 x 3 = 24  8 x 4 = 32  8 x 5 = 40  8 x 6 = 48  8 x 7 = 56  8 x 8 = 64  
9 x 1 = 9  9 x 2 = 18  9 x 3 = 27  9 x 4 = 36  9 x 5 = 45  9 x 6 = 54  9 x 7 = 63  9 x 8 = 72  9 x 9 = 81  
"""
######################################
"""
for i in range(1, 10):
    for j in range(1, i+1):
        if i != j:
            print('%d x %d = %d' % (i, j, i*j), end="  ")
        else:
            print('%d x %d = %d' % (i, j, i*j))

输出结果：
1 x 1 = 1
2 x 1 = 2  2 x 2 = 4
3 x 1 = 3  3 x 2 = 6  3 x 3 = 9
4 x 1 = 4  4 x 2 = 8  4 x 3 = 12  4 x 4 = 16
5 x 1 = 5  5 x 2 = 10  5 x 3 = 15  5 x 4 = 20  5 x 5 = 25
6 x 1 = 6  6 x 2 = 12  6 x 3 = 18  6 x 4 = 24  6 x 5 = 30  6 x 6 = 36
7 x 1 = 7  7 x 2 = 14  7 x 3 = 21  7 x 4 = 28  7 x 5 = 35  7 x 6 = 42  7 x 7 = 49
8 x 1 = 8  8 x 2 = 16  8 x 3 = 24  8 x 4 = 32  8 x 5 = 40  8 x 6 = 48  8 x 7 = 56  8 x 8 = 64
9 x 1 = 9  9 x 2 = 18  9 x 3 = 27  9 x 4 = 36  9 x 5 = 45  9 x 6 = 54  9 x 7 = 63  9 x 8 = 72  9 x 9 = 81
"""
######################################
"""
for i in range(1, 10):
    for j in range(1, i+1):
        if i != j:
            print('%d x %d = %d' % (j, i, i*j), end="  ")
        else:
            print('%d x %d = %d' % (j, i, i*j))

输出结果：正解
1 x 1 = 1
1 x 2 = 2  2 x 2 = 4
1 x 3 = 3  2 x 3 = 6  3 x 3 = 9
1 x 4 = 4  2 x 4 = 8  3 x 4 = 12  4 x 4 = 16
1 x 5 = 5  2 x 5 = 10  3 x 5 = 15  4 x 5 = 20  5 x 5 = 25
1 x 6 = 6  2 x 6 = 12  3 x 6 = 18  4 x 6 = 24  5 x 6 = 30  6 x 6 = 36
1 x 7 = 7  2 x 7 = 14  3 x 7 = 21  4 x 7 = 28  5 x 7 = 35  6 x 7 = 42  7 x 7 = 49
1 x 8 = 8  2 x 8 = 16  3 x 8 = 24  4 x 8 = 32  5 x 8 = 40  6 x 8 = 48  7 x 8 = 56  8 x 8 = 64
1 x 9 = 9  2 x 9 = 18  3 x 9 = 27  4 x 9 = 36  5 x 9 = 45  6 x 9 = 54  7 x 9 = 63  8 x 9 = 72  9 x 9 = 81
"""

######################################
"""
反面例子：
for a in range(1, 5):
    for b in range(1, 5):
        if a == b:
            continue
        for c in range(1, 5):
            if a == b or a == c:
                continue
            elif b == c:
                continue
            elif a == b == c:
                continue
        print("{}{}{}".format(a, b, c))

# https://gitee.com/crossin/crossincode/blob/master/num_comp/num_comp.py
# 本例程代码基于 Python 3！
# range(1, 5) 得到 1,2,3,4
# 三重循环挑出三个互不相同的数字i,j,k
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            # 如果i,j,k互不相等则输出到控制台
            if i != j and i != k and j != k:
                print(str(i)+str(j)+str(k))
"""
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if a != b and a != c and c != b:
                print("{}{}{}".format(a, b, c))
