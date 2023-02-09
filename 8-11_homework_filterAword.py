def add_words(words):
    #global blocked_words  # 如果在这个位置定义全局变量，则load_blocked()和words_filter(text, symbol='*')里的blocked_words都显示未定义，报错。为什么？
    words_1 = str(words + "\n")
    with open(r"practice\blocked_words.txt", "a", encoding="UTF-8") as blocked_words:
        blocked_words.write(words_1)
    print("已将'%s'添加至禁止词汇。" % words)


def load_blocked():
    global blocked_words  # 使用全局变量记录屏蔽词
    with open(r"practice\blocked_words.txt", encoding="UTF-8") as f:
        blocked_words = [l.strip() for l in f.readlines() if l]

def words_filter(text, symbol='*'):
    for w in blocked_words:
        text = text.replace(w, symbol * len(w))
    return text


judge = True

while judge:
    j = input("是否添加添加禁止词汇？(y/n)： ")
    if j == "n":
        judge = False
    else:
        add_words(input("添加一个禁止词汇：\n"))
        j = input("继续添加禁止词汇吗？(y/n)： ")

load_blocked()

while True:
    t = input('输入文字(直接回车退出)：\n')
    if not t:  # 如果 t 为空则跳出
        break
    print(words_filter(t))  # 输出替换结果