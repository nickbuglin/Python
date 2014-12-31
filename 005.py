# -*- coding: utf-8 -*-
import csv

data = [['1', '2', '3', '4', '5', '6'], ['2', '3', '4', '5', '6', '7']]
f = open("stock.csv","wb")
w = csv.writer(f)
w.writerows(data)
f.close()