######################################
# 【https://crossincode.com/school/lesson/75/】
# 7-18. 编程实例 - 三人斗地主手牌生成
"""
【问题描述】
三人斗地主手牌规则：

一副牌 54 张（4 种花色各 13 张，大小王），一人 17 张，留 3 张做底牌。

要求：
将一副牌随机打乱（洗牌）后分配给 3 位玩家（发牌），输出每个人的手牌和剩余底牌。

可使用 list 和 random 完成。
"""
import random

# 1. 生成54张牌的列表。
list_cards = ["JOKER", "joker"]
list_signs = ['♠', '♥', '♣', '♦']
list_numbers = ["2", "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3"]

for a in list_signs:
    for b in list_numbers:
        list_cards.append(a + b)

# 2. 随机打乱列表的机制。
random.shuffle(list_cards)
list_washed = list_cards[:]

# 3. 抽取17张牌(x3)，且剩余3张牌的机制。
li_plyer_1 = []
li_plyer_2 = []
li_plyer_3 = []

while len(list_washed) > 3:
    li_plyer_1.append(list_washed.pop())
    li_plyer_2.append(list_washed.pop())
    li_plyer_3.append(list_washed.pop())

print("plyer_1", len(li_plyer_1), li_plyer_1)
print("plyer_2", len(li_plyer_2), li_plyer_2)
print("plyer_3", len(li_plyer_3), li_plyer_3)
print("Hidden Cards", list_washed)
