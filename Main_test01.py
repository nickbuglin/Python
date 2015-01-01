#-*- coding: utf-8 -*-
import requests
from lxml import etree
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np

#-----------------------------------------------

# 偽裝為瀏覽器，所要加入的headers
headers = {'content-type': 'text/html; charset=utf-8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
# 要解析的網站對象
xurl = 'http://www.cnyes.com/twstock/finratio2/3481.htm'

r = requests.get(xurl,headers=headers)
r.encoding = 'utf-8'
#print (r.text)  #測試抓出來的HTML用

#------------------------------------------------------------------------------

page = etree.HTML(r.text)
writer = pd.ExcelWriter('stockXls\Stock.xlsx')
ro1 =['','','','','','']
ro2 =['','','','','','']
tRx = 3
tHx = 5
tDx = 5
dataset = []

for j in range(6,0,-1):
    sertxt = '//tr[2]/th[last()-'+ str(5-tHx) +']'
    hrefs = page.xpath(sertxt)
    for href in hrefs:
        ro1[tHx]=href.text
    tHx -= 1

for i in range(2,50,1):
    for k in range(6,0,-1):
        sertxt = '//tr['+ str(tRx) +']/td[last()-'+ str(5-tDx) +']'
        hrefs = page.xpath(sertxt)
        for href in hrefs:
            ro2[tDx]=href.text
        tDx -= 1
    tRx += 1
    tDx = 5
    dset = [(ro2[0],ro2[1],ro2[2],ro2[3],ro2[4],ro2[5])]
    dataset = dataset + dset

df = pd.DataFrame(data=dataset, columns=[ro1[0],ro1[1],ro1[2],ro1[3],ro1[4],ro1[5]])
df.info()
df.to_excel(writer,'finratio2', index=False)

writer.save()

#------------------------------------------------------------------------------







