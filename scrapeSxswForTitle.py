#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 22:54:06 2018

@author: evan
"""

def scrapeSxswForTitle(html,yourTitle): #program does nothing as written
    
    from bs4 import BeautifulSoup
    import requests
    import csv
    
    print(html)
    print(yourTitle)