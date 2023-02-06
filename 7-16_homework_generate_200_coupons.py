######################################
#7-16. 编程实例 - 生成优惠券号码
#【https://crossincode.com/school/lesson/74/】
"""
【问题描述】
很多付费应用的开发者，会设计一些优惠券来吸引用户来使用新开发的应用，以达到一定的广告效应。

现在，请你帮他们设计并生成200个优惠券号码：

・优惠码的字符由26个英文字符（大小写）组成
・每个优惠码有8位
"""
import string
import random

a_list = list(string.ascii_letters)
Coupon_list = []

while len(Coupon_list) != 200:
    random.shuffle(a_list)
    i = random.randint(0, 53)
    str_1 = "".join(a_list[i:i + 8])
    if str_1 in Coupon_list:
        pass
    elif i > 44:
        pass
    else:
        Coupon_list.append(str_1)

print(len(Coupon_list))
print(Coupon_list)



