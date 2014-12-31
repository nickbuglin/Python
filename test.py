#-*- coding: utf-8 -*-
from pyquery import PyQuery as pq
from lxml import etree
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


headers = {'content-type': 'text/html; charset=utf-8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

xurl = 'http://www.goodinfo.tw/stockinfo/StockDetail.asp?STOCK_ID=3481'

v_source = pq(xurl, headers=headers)


print v_source.text()
#print v_source.text().decode('UTF-16LE').encode('UTF-8')



f = open("stock.csv","wb")

f.write('\xEF\xBB\xBF')
for data in v_source('tr'):

    for data_th in pq(data).find('th'):
        ro1 = pq(data).find('th').eq(0).text()
        ro2 = pq(data).find('th').eq(1).text()
        ro3 = pq(data).find('th').eq(2).text()
        ro4 = pq(data).find('th').eq(3).text()
        ro5 = pq(data).find('th').eq(4).text()
        ro6 = pq(data).find('th').eq(5).text()

    for data_th in pq(data).find('td'):
        ro1 = pq(data).find('td').eq(0).text()
        ro2 = pq(data).find('td').eq(1).text()
        ro3 = pq(data).find('td').eq(2).text()
        ro4 = pq(data).find('td').eq(3).text()
        ro5 = pq(data).find('td').eq(4).text()
        ro6 = pq(data).find('td').eq(5).text()

    writedata = [[ro1, ro2, ro3, ro4, ro5, ro6]]
    w = csv.writer(f)
    w.writerows(writedata)

f.close()

"""
    for i in range(len(pq(v_ind).find('a'))):
        v_indname = pq(v_ind).find('a').eq(i).text()
        print v_code
        print v_name
        print v_indname
"""