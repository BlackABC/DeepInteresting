# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:23:38 2019

@author: Administrator
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

# 打开文本
text = open("tzfszj.txt", encoding = 'utf8').read()

#中文分词
text = ' '.join(jieba.cut(text))
print(text[:100])

# 生成词云
wc = WordCloud(font_path = 'Hiragino.ttf', width = 800, height = 600,
               mode = 'RGBA', background_color = None).generate(text)

# 显示词云
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()

wc.to_file("fctzfszj.png")