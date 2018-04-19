#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 21:48:13 2018

@author: evan
"""

from bs4 import BeautifulSoup
import requests
import csv

# Purpose: scrape Title information from all 2018 SXSW featured events. 
# Also scrape Title information from all 2017 SXSW featured events.
# Compare the amount of times the words 'artificial intelligence' / 'AI' appeared in the titles of both
# https://schedule.sxsw.com/2017/events/category/featured

csv_file = open('SXSW_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)

def scrapeSxswForTitle(html,yourTitle): #program does nothing as written
    
    source = requests.get(html).text
    soup = BeautifulSoup(source, 'lxml')
    csv_writer.writerow([yourTitle]) 
    article = soup.find('article')
    
    for eventTitle in article.find_all('div',class_='row single-event'):
    
        try:
            eventTitle = eventTitle.a.text
        
        except Exception as e:
            eventTitle = 'None'
        print(eventTitle)
    
        csv_writer.writerow([eventTitle])

    csv_writer.writerow([' '])
    csv_writer.writerow([' '])

# Mar 10 - Mar 19, 2017
scrapeSxswForTitle('https://schedule.sxsw.com/2017/events/category/featured','featured sessions 2017')

scrapeSxswForTitle('https://schedule.sxsw.com/2017/3/10/events/type/panel','Panel Talks Mar 10 2017')
scrapeSxswForTitle('https://schedule.sxsw.com/2017/3/11/events/type/panel','Panel Talks Mar 11 2017')
scrapeSxswForTitle('https://schedule.sxsw.com/2017/3/12/events/type/panel','Panel Talks Mar 12 2017')
scrapeSxswForTitle('https://schedule.sxsw.com/2017/3/13/events/type/panel','Panel Talks Mar 13 2017')
scrapeSxswForTitle('https://schedule.sxsw.com/2017/3/14/events/type/panel','Panel Talks Mar 14 2017')
scrapeSxswForTitle('https://schedule.sxsw.com/2017/3/15/events/type/panel','Panel Talks Mar 15 2017')
scrapeSxswForTitle('https://schedule.sxsw.com/2017/3/16/events/type/panel','Panel Talks Mar 16 2017')
scrapeSxswForTitle('https://schedule.sxsw.com/2017/3/17/events/type/panel','Panel Talks Mar 17 2017')
scrapeSxswForTitle('https://schedule.sxsw.com/2017/3/18/events/type/panel','Panel Talks Mar 18 2017')
scrapeSxswForTitle('https://schedule.sxsw.com/2017/3/19/events/type/panel','Panel Talks Mar 19 2017')


# Mar 9 - Mar 18, 2018
scrapeSxswForTitle('https://schedule.sxsw.com/2018/events/category/featured','featured sessions 2018')

scrapeSxswForTitle('https://schedule.sxsw.com/2018/3/9/events/type/panel','Panel Talks Mar 9 2018')
scrapeSxswForTitle('https://schedule.sxsw.com/2018/3/10/events/type/panel','Panel Talks Mar 10 2018')  
scrapeSxswForTitle('https://schedule.sxsw.com/2018/3/11/events/type/panel','Panel Talks Mar 11 2018')  
scrapeSxswForTitle('https://schedule.sxsw.com/2018/3/12/events/type/panel','Panel Talks Mar 12 2018')  
scrapeSxswForTitle('https://schedule.sxsw.com/2018/3/13/events/type/panel','Panel Talks Mar 13 2018')  
scrapeSxswForTitle('https://schedule.sxsw.com/2018/3/14/events/type/panel','Panel Talks Mar 14 2018')  
scrapeSxswForTitle('https://schedule.sxsw.com/2018/3/15/events/type/panel','Panel Talks Mar 15 2018')  
scrapeSxswForTitle('https://schedule.sxsw.com/2018/3/16/events/type/panel','Panel Talks Mar 16 2018')  
scrapeSxswForTitle('https://schedule.sxsw.com/2018/3/17/events/type/panel','Panel Talks Mar 17 2018')  
scrapeSxswForTitle('https://schedule.sxsw.com/2018/3/18/events/type/panel','Panel Talks Mar 18 2018')  

csv_file.close()
