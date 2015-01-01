#-*- coding: utf-8 -*-
import requests
from lxml import etree
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np

#-----------------------------------------------

filename = 'stockXls\\twse.xlsx'
writer = pd.ExcelWriter(filename)

# 偽裝為瀏覽器，所要加入的headers
headers = {'content-type': 'text/html; charset=utf-8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
# 要解析的網站對象
#xurl = 'http://www.cnyes.com/twstock/profile/' + stocknum + '.htm'
xurl = 'http://www.twse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU_d.php'

r = requests.get(xurl,headers=headers)
r.encoding = 'big5'
#print (r.text)  #測試抓出來的HTML用

#------------------------------------------------------------------------------

page = etree.HTML(r.text)
ro1 =['','','','','']
ro2 =['','','','','']
tRx = 21
tHx = 4
tDx = 4
dataset = []

for j in range(5,0,-1):
    sertxt = '//tr/th[last()-'+ str(4-tHx) +']'
    hrefs = page.xpath(sertxt)
    for href in hrefs:
        ro1[tHx]=href.text
    tHx -= 1

for i in range(0,849,1):
    for k in range(6,0,-1):
        sertxt = '//tr['+ str(tRx) +']/td[last()-'+ str(4-tDx) +']'
        hrefs = page.xpath(sertxt)
        for href in hrefs:
            ro2[tDx]=href.text
        tDx -= 1
    tRx += 1
    tDx = 5
    dset = [(ro2[0],ro2[1],ro2[2],ro2[3],ro2[4])]
    dataset = dataset + dset

df_BWIBBU = pd.DataFrame(data=dataset, columns=[ro1[0],ro1[1],ro1[2],ro1[3],ro1[4]])
df_BWIBBU.info()
df_BWIBBU.to_excel(writer,'BWIBBU', index=False)

writer.save()

#------------------------------------------------------------------------------







