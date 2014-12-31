#-*- coding: utf-8 -*-
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import csv
import sys
from html.parser import HTMLParser


headers = {'content-type': 'text/html; charset=utf-8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

xurl = 'http://www.cnyes.com/twstock/profile/3481.htm'

r = requests.get(xurl,headers=headers)
#r.encoding = 'utf-8'



#------------------------------------------------------------------------------

f = open("stock.csv","w")
class hp(HTMLParser):
    a_text = False

    def handle_starttag(self,tag,attr):
        if tag == 'tr':
            self.a_text = True
            #print (dict(attr))

    def handle_endtag(self,tag):
        if tag == 'td':
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
