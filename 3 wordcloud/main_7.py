# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:17:50 2019

@author: Administrator
"""

from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import jieba.analyse

text = open('xyj.txt', encoding = 'utf8').read()

# 提取关键词和权重
freq = jieba.analyse.extract_tags(text, topK=200, withWeight=True)
print(freq[:20])
freq = {i[0]: i[1] for i in freq}

mask = np.array(Image.open("color_mask.png"))
wc = WordCloud(mask = mask, font_path='Hiragino.ttf', mode = 'RGBA',
               background_color = None).generate_from_frequencies(freq)

image_colors = ImageColorGenerator(mask)
wc.recolor(color_func=image_colors)

plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()

wc.to_file("freaxyj.png")