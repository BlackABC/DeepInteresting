# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:37:57 2019

@author: Administrator
"""

from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba

# 打开文本
text = open("xyj.txt", encoding = 'utf8').read()

# 分词
text = ' '.join(jieba.cut(text))

#生成词云
mask = np.array(Image.open("black_mask.png"))
wc = WordCloud(mask = mask, font_path = 'Hiragino.ttf', mode = 'RGBA', 
               background_color = None).generate(text)

# 显示词云
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()

# 保存词云
wc.to_file("maskxyj.png")