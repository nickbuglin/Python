
#############################################
# READ STOCK PRICE FROM FINANCE.YAHOO.COM   #
#############################################
from urllib import request
import urllib
from dateutil.relativedelta import *
from datetime import *
def GetPrice(ticker, start, end):

stock = ticker.upper()

m1 = int(start.split("/")[0])
d1 = int(start.split("/")[1])
y1 = int(start.split("/")[2])
dt1 = date(y1, m1, d1) + relativedelta(months = -1)
a = dt1.month
b = dt1.day
c = dt1.year

m2 = int(end.split("/")[0])
d2 = int(end.split("/")[1])
y2 = int(end.split("/")[2])
dt2 = date(y2, m2, d2) + relativedelta(months = -1)
d = dt2.month
e = dt2.day
f = dt2.year

url = "http://ichart.finance.yahoo.com/table.csv?s=" + stock + \
"&d=" + str(d) + "&e=" + str(e) + "&f=" + str(f) +       \
"&g=d&a=" + str(a) + "&b=" + str(b) + "&c=" + str(c) + "&ignore=.csv"
data = request.urlopen(url)
print (data.read())

GetPrice("jpm", "08/01/2009", "08/10/2009")