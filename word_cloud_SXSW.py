#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 12:46:48 2018

@author: evan
"""

# Purpose: Read in csv of SXSW titles.  Create a word-cloud.
#
# Input: csv path
#
# Output: word cloud 
#
from os import path
from wordcloud import WordCloud
import numpy as np
from PIL import Image
d = path.dirname(__file__)


print('Start 2017 Wordcloud')
# Read the whole text.
mask = np.array(Image.open(path.join(d, "SXSW2017.png")))

text = open(path.join(d, 'SXSW_scrape_2017.csv')).read()
wordcloud = WordCloud(max_words=1000,max_font_size=2200,width=2400,height=1600,mask=mask,background_color='white').generate(text)
# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear', aspect='auto') # aspect auto did nothing
plt.axis("off")
#plt.figure(figsize=(20,10))
wordcloud.to_file("SXSW2017_WC.png")
plt.show()
print(wordcloud.width)
print(wordcloud.height)
print('2017 Wordcloud Complete')
# lower max_font_size
#wordcloud = WordCloud(max_font_size=40,width=2400,height=1600).generate(text)
#plt.figure()
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")

print('Start 2018 Wordcloud')
mask = np.array(Image.open(path.join(d, "SXSW2018.png")))
text2 = open(path.join(d, 'SXSW_scrape_2018.csv')).read()
wordcloud2 = WordCloud(max_words=1000,max_font_size=2200,width=2400,height=1600,mask=mask,scale=2).generate(text2)

plt.imshow(wordcloud2, interpolation='bilinear', aspect='auto')
plt.axis("off")
#plt.figure(figsize=(20,10))
wordcloud2.to_file("SXSW2018_WC.png")
print('2018 Wordcloud Complete')
plt.show()


# Good code below
# import csv
#with open('SXSW_scrape.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))


