#coding=utf-8
from pyquery import PyQuery as pq
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 偽裝為瀏覽器，加入Headers
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
# 目標網頁
xurl = 'http://www.cnyes.com/twstock/ps_historyprice/3481.htm'

v_source = pq(xurl, headers=headers)

#print v_source.text()


for data in v_source('tr'):
    print pq(data).find('td').eq(0).text()
    print pq(data).find('td').eq(1).text()
    print pq(data).find('td').eq(2).text()
    print pq(data).find('td').eq(3).text()
    print pq(data).find('td').eq(4).text()
    print pq(data).find('td').eq(5).text()

"""
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