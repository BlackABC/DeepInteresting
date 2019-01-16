# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:47:12 2019

@author: Administrator
"""

from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import jieba

text = open("xyj.txt", encoding = 'utf8').read()

text = ' '.join(jieba.cut(text))

mask = np.array(Image.open('color_mask.png'))
wc = WordCloud(mask = mask, font_path = 'Hiragino.ttf', mode = 'RGBA', 
               background_color = None).generate(text)

# 从图片中生成颜色
image_colors = ImageColorGenerator(mask)
wc.recolor(color_func = image_colors)

plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()

wc.to_file("cmxyj.png")