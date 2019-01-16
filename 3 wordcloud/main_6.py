# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:02:21 2019

@author: Administrator
"""

from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import random
import jieba

text = open("xyj.txt", encoding = 'utf8').read()

text = ' '.join(jieba.cut(text))

# 颜色函数
def random_color(word, font_size, position, orientation, font_path, random_state):
    s = 'hsl(0, %d%%, %d%%)' % (random.randint(60, 80), random.randint(60, 80))
    print(s)
    return s

mask = np.array(Image.open("color_mask.png"))
wc = WordCloud(color_func = random_color, mask = mask, font_path = 'Hiragino.ttf', mode = 'RGBA', 
               background_color = None).generate(text)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

wc.to_file('cccmxyj.png')