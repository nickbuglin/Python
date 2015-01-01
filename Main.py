#-*- coding: utf-8 -*-
import requests
from lxml import etree
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np

#--------------[ 全 域 初 始 化 ]------------------------------------------------------------------

writer = pd.ExcelWriter('stockXls\Stock.xlsx')

#--------------[ 第一段：取得基本資料intro ]-----------------------------------------------------

# 偽裝為瀏覽器，所要加入的headers
headers = {'content-type': 'text/html; charset=utf-8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
# 要解析的網站對象
xurl = 'http://www.cnyes.com/twstock/intro/3481.htm'
# 使用requests抓出HTML
r = requests.get(xurl,headers=headers)
# 轉碼為'utf-8'
r.encoding = 'utf-8'

#------------------------------------
# 帶入lxml解析
page = etree.HTML(r.text)
# 初始化 ro1 list
ro1 =['','','','','']
# 取得 公司簡稱 資料
hrefs = page.xpath("//tr[2]/td[2]/span")
for href in hrefs:
    ro1[0] = href.text
# 取得 董事長 資料
hrefs = page.xpath("//tr[4]/td[2]/span")
for href in hrefs:
    ro1[1] = href.text
# 取得 上市日期 資料
hrefs = page.xpath("//tr[16]/td[2]/span")
for href in hrefs:
    ro1[2] = href.text
# 取得 資本額 資料
hrefs = page.xpath("//tr[17]/td[1]/span")
for href in hrefs:
    ro1[3] = href.text
# 取得 發行股數 資料
hrefs = page.xpath("//tr[18]/td[1]/span")
for href in hrefs:
    ro1[4] = href.text
# ro1 list 帶入 dataset
dataset = [(ro1[0],ro1[1],ro1[2],ro1[3],ro1[4])]
# 資料集寫入 intro頁籤
df_instro = pd.DataFrame(data=dataset, columns=['公司簡稱','董事長','上市日期','資本額','發行股數'])
df_instro.to_excel(writer,'intro', index=False)

#---------------------[ 第二段：取得季度財務比率finratio ]---------------------------------------------------------

# 偽裝為瀏覽器，所要加入的headers
headers = {'content-type': 'text/html; charset=utf-8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
# 要解析的網站對象
xurl = 'http://www.cnyes.com/twstock/finratio/3481.htm'
# 使用requests抓出HTML
r = requests.get(xurl,headers=headers)
# 轉碼為'utf-8'
r.encoding = 'utf-8'
#print (r.text)  #測試抓出來的HTML用

#------------------------------
# 帶入lxml解析
page = etree.HTML(r.text)
# 初始化資料
ro1 =['','','','','','']
ro2 =['','','','','','']
tRx = 3
tHx = 5
tDx = 5
dataset = []
# 抓出標題列，放到ro1 list，從最尾端往上抓資料
for j in range(6,0,-1):
    # 設定搜尋條件
    sertxt = '//tr[2]/th[last()-'+ str(5-tHx) +']'
    hrefs = page.xpath(sertxt)
    for href in hrefs:
        ro1[tHx]=href.text
    tHx -= 1
# 抓出剩下全部資料，從最尾端往上抓資料，陸續塞到dataset
for i in range(2,44,1):
    for k in range(6,0,-1):
        # 設定搜尋條件
        sertxt = '//tr['+ str(tRx) +']/td[last()-'+ str(5-tDx) +']'
        hrefs = page.xpath(sertxt)
        for href in hrefs:
            ro2[tDx]=href.text
        tDx -= 1
    tRx += 1
    tDx = 5
    dset = [(ro2[0],ro2[1],ro2[2],ro2[3],ro2[4],ro2[5])]
    dataset = dataset + dset
# 資料集寫入 finratio頁籤
df_finratio = pd.DataFrame(data=dataset, columns=[ro1[0],ro1[1],ro1[2],ro1[3],ro1[4],ro1[5]])
df_finratio.info()
df_finratio.to_excel(writer,'finratio', index=False)

#---------------------[ 第二段：取得季度財務比率finratio ]---------------------------------------------------------

# 偽裝為瀏覽器，所要加入的headers
headers = {'content-type': 'text/html; charset=utf-8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
# 要解析的網站對象
xurl = 'http://www.cnyes.com/twstock/finratio/3481.htm'
# 使用requests抓出HTML
r = requests.get(xurl,headers=headers)
# 轉碼為'utf-8'
r.encoding = 'utf-8'
#print (r.text)  #測試抓出來的HTML用

#------------------------------
# 帶入lxml解析
page = etree.HTML(r.text)
# 初始化資料
ro1 =['','','','','','']
ro2 =['','','','','','']
tRx = 3
tHx = 5
tDx = 5
dataset = []
# 抓出標題列，放到ro1 list，從最尾端往上抓資料
for j in range(6,0,-1):
    # 設定搜尋條件
    sertxt = '//tr[2]/th[last()-'+ str(5-tHx) +']'
    hrefs = page.xpath(sertxt)
    for href in hrefs:
        ro1[tHx]=href.text
    tHx -= 1
# 抓出剩下全部資料，從最尾端往上抓資料，陸續塞到dataset
for i in range(2,46,1):
    for k in range(6,0,-1):
        # 設定搜尋條件
        sertxt = '//tr['+ str(tRx) +']/td[last()-'+ str(5-tDx) +']'
        hrefs = page.xpath(sertxt)
        for href in hrefs:
            ro2[tDx]=href.text
        tDx -= 1
    tRx += 1
    tDx = 5
    dset = [(ro2[0],ro2[1],ro2[2],ro2[3],ro2[4],ro2[5])]
    dataset = dataset + dset
# 資料集寫入 finratio頁籤
df_finratio2 = pd.DataFrame(data=dataset, columns=[ro1[0],ro1[1],ro1[2],ro1[3],ro1[4],ro1[5]])
df_finratio2.info()
df_finratio2.to_excel(writer,'finratio2', index=False)

#---------------------[ 全 域 收 尾 處 理 ]-----------------------------------------------------------------
# 儲存excel檔案
writer.save()
