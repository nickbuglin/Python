#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: writecsv.py
#Author: xiaobing
#E-mail: xiaobingzhang29@gmail.com
#Date: 2013-11-02
#Description: 

import csv

def getSortedValues(row):
    sortedValues = []
    keys = row.keys()
    keys.sort()
    for key in keys:
        sortedValues.append(row[key])
    
    return sortedValues


ro1 = 4
ro2 = 5

rows = [{'Colum1': ro1, 'Column2': ro2, 'Column3': '2', 'Column4': '3'},
        {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
        {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
        {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'}]


fieldnames = {'Column1':'栏目1', 'Column2':'栏目2', 'Column3':'栏目3', 'Column4':'栏目4'}
csvFile = 'csvFile.csv'
fileobj = open(csvFile, 'wb')

# 先写入几个字符,防止windows乱码
fileobj.write('\xEF\xBB\xBF')
writer = csv.writer(fileobj,dialect='excel')

# 先写入头信息
sortedValues = getSortedValues(fieldnames)
writer.writerow(sortedValues)

# 将数据逐行写入
for row in rows:
    sortedValues = getSortedValues(row)
    writer.writerow(sortedValues) 
