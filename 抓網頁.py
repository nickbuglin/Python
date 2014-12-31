#coding=utf-8
from pyquery import PyQuery as pq
from lxml import etree

headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

v_source=pq(url='http://www.ruten.com.tw/', headers=headers)


print v_source.text()


for data in v_source('tr'):
    v_code = pq(data).find('td').eq(0).text()
    v_name = pq(data).find('td').eq(1).text()
    v_ind = pq(data).find('td').eq(5)

    for i in range(len(pq(v_ind).find('a'))):
        v_indname = pq(v_ind).find('a').eq(i).text()
        print v_code
        print v_name
        print v_indname