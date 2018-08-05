#实战练习之制作词云#

代码思路：
用了两个函数，word_segment（分词）和generate_wordCloud（生成词云）

具体代码思路如下：
1、分词：读取文本文件的人物事迹内容，使用jieba进行分词；
2、生成词云：读取背景图片，设置背景颜色、背景图片，同时设置能够兼容中文字体，以免出现乱码。最后就是根据分词后的文本内容生成词云并将图片保存到本地。

总结：
代码写得比较简单，本来想多做一些处理，做得更为精美一些，不过最近工作太忙了，难得周末，还是想多留点时间学习一下其它东西，就不追求高质量了，练练手就好。
这次的作业题目蛮有趣的，之前总是在网上看到类似的词云，觉得很酷炫，但是没有尝试做过，今天看到最终输出的图片，还是觉得蛮开心的。
生活总是不乏乐趣，编程亦是如此。


代码如下：

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import numpy as np
from PIL import Image

# 分词
def word_segment(fileName):
    with open(fileName, 'r', encoding='utf-8') as f:
        myText = f.read()
    myText = " ".join(jieba.cut(myText))    # 使用jieba进行分词

    return myText

def generate_wordCloud(myText):
    # 读取背景图片
    hugo_mask = np.array(Image.open("hugo_mask.jpg"))
    wordCloud = WordCloud(background_color = "white",     # 设置背景颜色
                          mask = hugo_mask,  # 设置背景图片
                          font_path = "simsun.ttf"        # 兼容中文字体，不然中文会显示乱码
                          )
    wordCloud.generate(myText)  # 生成词云
    wordCloud.to_file('hugo.jpg')   # 保存图片到本地

    plt.imshow(wordCloud, interpolation='bilinear')     # 绘制词云
    plt.axis("off")     #不显示坐标尺寸
    plt.show()  # 展现词云

if __name__ == '__main__':
    fileName = 'hugo.txt'
    myText = word_segment(fileName)
    generate_wordCloud(myText)