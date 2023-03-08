from PyDictionary import PyDictionary

dictionary=PyDictionary()

while True:
    word = input("请输入您要查询的单词：")
    if word.lower() == "exit":
        break
    meaning = dictionary.meaning(word)
    if meaning is None:
        print("没有找到该单词的含义，请重新输入")
    else:
        print("【%s】的含义：" % word)
        for part_of_speech, definitions in meaning.items():
            print("%s:" % part_of_speech.capitalize())
            for i, definition in enumerate(definitions, start=1):
                print("%d. %s" % (i, definition))
#在运行程序之后，程序会提示您输入要查询的单词，
# 如果输入的单词在字典中存在，程序会输出该单词的含义；
# 如果输入的单词不存在，程序会提示您重新输入。                