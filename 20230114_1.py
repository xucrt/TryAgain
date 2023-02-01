print('hello worllllllld')
print(3e30, end="") # 【end=""】后面不换行
print(2 > 5) # 输出值为【False】。因上一行命令末尾有【end=""】，所以False紧贴着上一行的输出值【3e+30】
print('hello', 'nworld', 'npython')
print('hello\nworld\npython')
######################################

x = int(input())  # 转换成整数
print(x)

y = float(input())  # 转换成小数
print(y)

z = eval(input())   # 通用转换
print(z)

print("你今晚吃的啥?")
g = str(input())   # 转换成文字列
print(g, "的味道咋样呀？")

######################################

print("ChuXu")
print(1+2-3*4/5)
print("兎", end="")
print("年")
print("Start Over\nPython")