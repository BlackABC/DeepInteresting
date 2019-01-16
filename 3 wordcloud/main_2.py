# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 15:27:41 2019

@author: Administrator
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = open("tzfszj.txt", encoding = 'utf8').read()
wc = WordCloud(font_path='Hiragino.ttf', width = 800, height = 600, mode = 'RGBA', background_color = None).generate(text)

plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()

wc.to_file('tzfszj.png')