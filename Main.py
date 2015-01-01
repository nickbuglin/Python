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
xurl = 'http://www.cnyes.com/twstock/intro/3481.htm'

r = requests.get(xurl,headers=headers)
r.encoding = 'utf-8'
#print (r.text)  #測試抓出來的HTML用

#------------------------------------------------------------------------------
page = etree.HTML(r.text)
hrefs = page.xpath("//th | //tr/td/span")

writer = pd.ExcelWriter('stockXls\Stock.xlsx')
txtCon = ''
ro1 =['','','','','']
ro2 =['','','','','']

for href in hrefs:
    #print (href.text)  #測試抓出來的文字用
    if href.text:
        if href.text == '公司簡稱':
            txtCon = href.text
        if txtCon == '公司簡稱' and txtCon != href.text:
            ro1[0] = txtCon
            ro2[0] = href.text
            txtCon = ''
        if href.text == '董事長':
            txtCon = href.text
        if txtCon == '董事長' and txtCon != href.text:
            ro1[1] = txtCon
            ro2[1] = href.text
            txtCon = ''
        if href.text == '上市日期':
            txtCon = href.text
        if txtCon == '上市日期' and txtCon != href.text:
            ro1[2] = txtCon
            ro2[2] = href.text
            txtCon = ''
        if href.text == '實收資本額':
            txtCon = href.text
        if txtCon == '實收資本額' and txtCon != href.text:
            ro1[3] = txtCon
            ro2[3] = href.text
            txtCon = ''
        if href.text == '普通股發行股數':
            txtCon = href.text
        if txtCon == '普通股發行股數' and txtCon != href.text:
            ro1[4] = txtCon
            ro2[4] = href.text
            txtCon = ''

dataset = [(ro2[0],ro2[1],ro2[2],ro2[3],ro2[4])]
df = pd.DataFrame(data=dataset, columns=[ro1[0],ro1[1],ro1[2],ro1[3],ro1[4]])
df.info()
df.to_excel(writer,'intro', index=False)

#------------------------------------------------------------------------------







writer.save()
