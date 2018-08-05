import os
import docx
import string

def read_file_content(filePath):
    fileList = []
    # 将文件夹下的所有文件名读取到fileList
    for f in os.listdir(filePath):
        fileList.append(f)

    contentList = []
    # 外循环遍历每一个文档，将文档内容存储到content
    for fileName in fileList:
        content = docx.Document(filePath + fileName)
        # 内循环遍历每个文档的所有段落，将文档内容存储到contentList
        for para in content.paragraphs:
            contentList.append(para.text)

    return contentList

def count_words(contentList):
    wordsCount = {}
    # 外循环遍历每一个文档的内容，将处理后的文档数据存储到wordList
    for cl in contentList:
        # 不太会处理特殊符号，采用最简单粗暴的方法去掉各种标点符号、空格和中文字符
        wordList = cl.replace('.', '').replace('?', '').replace('-', '').replace('_', '').replace('()',
                        '').replace('(', '').replace(')', '').replace('[', '').replace(':', '').replace(']', '')
        wordList = wordList.strip(string.punctuation + string.whitespace)
        wordList = "".join(i for i in wordList if ord(i) < 127)
        # 内循环遍历wordList，统计每个单词的数量
        for word in wordList.strip().split():
            # 如果是新单词，则新增一个key，value赋值为1
            if word not in wordsCount:
                wordsCount[word] = 1
            # 如果是旧单词，则将key值对应的value值+1
            else:
                wordsCount[word] += 1

    # 生成以元组为元素的列表
    # key=lambda v: v[1]，表示将结果按键值排序
    new_wordCount = sorted(wordsCount.items(), key=lambda v: v[1])

    wordsNum = 0
    # 循环输出('单词',该单词的频次)
    for i in new_wordCount:
        print(i)
        wordsNum += i[1]
    print('共有单词：', wordsNum)

def main():
    filePath = "docx_files\\"
    contentList = read_file_content(filePath)
    count_words(contentList)

if __name__ == '__main__':
    main()