######################################
#7-15. 编程实例 - 统计单词出现次数
#https://crossincode.com/school/lesson/205/
"""
【问题描述】
有一个全部由字符串组成的列表 list_s，统计列表中每个单词出现的次数。
示例：
list_s = ['Beautiful', 'is', 'better', 'than', 'ugly', 'Explicit', 'is', 'better', 'than', 'implicit']
输出
{'Beautiful': 1, 'is': 2, 'better': 2, 'than': 2, 'ugly': 1, 'Explicit': 1, 'implicit': 1}
"""

list_s = ['Beautiful', 'is', 'better', 'than', 'ugly', 'Explicit', 'is', 'better', 'than', 'implicit']
list_2 = list(set(list_s))
dict_1 = {}

for a in range(len(list_2)):
    str_1 = list_2[a]
    dict_1[str_1] = 0

for b in range(len(list_s)):
    str_1 = list_s[b]
    if str_1 in dict_1:
        dict_1[str_1] = dict_1[str_1]+1
print(dict_1)
