#逻辑判断
num = 10
print('Guess what I think?')
answer = int(input())

result = answer<num
print('too small?')
print(result)

result = answer>num
print('too big?')
print(result)

result = answer==num
print('equal?')
print(result)

######################################
#字符串
name = "keke"
score = 66

print(f"{name}'s score is {score}!!")

#############################
#【https://crossincode.com/school/lesson/42/】
name = 'Crossin'
age = 18
code = 'Python'

# 通过 % 将 name, age, code 拼接成一句话
# 输出 Crossin is 18, he write Python.
result = "%s was %d, he plays %s." % (name, age, code)
print(result)

######################################

print("He said, \"I\'m yours!\"")
print("\\\\_v_//")
print("Stay hungry,\nstay foolish. \n\t -- Steve Jobs")
print("*\n***\n*****\n***\n*")

######################################
#a:hello,word; b:1.41; c:True; d:False; e:True

a = 'hello,world'
b = 1.414
c = (1 != 2)
d = (True and False)
e = (True or False)

result1 = f"a:{a} "
result2 = f"c:{c}; d:{d}; e:{e}"

#print(result2)
print(result1 + "b:%.2f " % b + result2)

######################################

h = '''\
\'hello,world\'
\\\"hello,world\"
'''
print(h)












