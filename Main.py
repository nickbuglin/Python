#-*- coding: utf-8 -*-
import requests
from lxml import etree



headers = {'content-type': 'text/html; charset=utf-8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

xurl = 'http://www.goodinfo.tw/stockinfo/StockDetail.asp?STOCK_ID=3481'

r = requests.get(xurl,headers=headers)
r.encoding = 'utf-8'
#print (r.text)

#------------------------------------------------------------------------------

page = etree.HTML(r.text)
hrefs = page.xpath("//tr/td/nobr | //tr//td")


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
            print (ro1,ro2)



#------------------------------------------------------------------------------
