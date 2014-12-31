#-*- coding: utf-8 -*-
import requests
from lxml import etree
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np

#-----------------------------------------------

headers = {'content-type': 'text/html; charset=utf-8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

xurl = 'http://www.goodinfo.tw/stockinfo/StockDetail.asp?STOCK_ID=3481'

r = requests.get(xurl,headers=headers)
r.encoding = 'utf-8'
#print (r.text)

#------------------------------------------------------------------------------
page = etree.HTML(r.text)
hrefs = page.xpath("//tr/td/nobr | //tr//td")


#np.seed(111)
txtCon = ''
ro1 =''
ro2 =''
ro3 =''
ro4 =''

for href in hrefs:

    if href.text:
         #print (href.text)
        if href.text == '名稱':
            txtCon = href.text
        if txtCon == '名稱' and txtCon != href.text:
            ro1 = txtCon
            ro2 = href.text
            #print (ro1,ro2)

            dataset = [(ro2)]
            df = pd.DataFrame(data=dataset, columns=[ro1])
            df.info()
            df.to_excel('Stock.xlsx', index=False)
            txtCon = ''

#------------------------------------------------------------------------------
"""
dataset = CreateDataSet(4)
df = pd.DataFrame(data=dataset, columns=['欄位一','狀態','自訂欄位','StatusDate'])
df.info()

# Save results to excel
df.to_excel('Lesson3.xlsx', index=False)
print ('Done')
"""