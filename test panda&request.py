#-*- coding: utf-8 -*-
from pyquery import PyQuery as pq
from lxml import etree
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import csv
import sys
from html.parser import HTMLParser


headers = {'content-type': 'text/html; charset=utf-8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
xurl = 'http://www.goodinfo.tw/stockinfo/StockDetail.asp?STOCK_ID=3481'

r = requests.get(xurl,headers=headers)
r.encoding = 'utf-8'

v_source = pq(r.text)

#print (v_source.text())

for data in v_source('tr'):
    ro1 = pq(data).find('td').eq(0).text()
    #print (ro1)

#------------------------------------------------------------------------------

f = open("stock.csv","w")
class hp(HTMLParser):
    a_text = False

    def handle_starttag(self,tag,attr):
        if tag == 'a':
            self.a_text = True
            #print (dict(attr))

    def handle_endtag(self,tag):
        if tag == 'a':
            self.a_text = False

    def handle_data(self,data):
        if self.a_text:
            print (data)
            writedata = [[data]]
            w = csv.writer(f)
            w.writerows(writedata)


yk = hp()
yk.feed(r.text)
yk.close()


f.close()
