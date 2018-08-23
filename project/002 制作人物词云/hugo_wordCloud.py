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