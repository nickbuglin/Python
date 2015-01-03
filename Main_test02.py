#-*- coding: utf-8 -*-
import requests
from lxml import etree
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np

tes = pd.read_excel('stockXls\\twse.xlsx', 'BWIBBU', index_col=None, parse_cols=0, na_values=['NA'])

for i in tes.index:
    print(tes['證券代號'][i])









