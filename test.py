
from urllib import request
from datetime import datetime

def GetHistory(ticker):
    stock = ticker + '.TW'
    d = datetime.now().month
    e = datetime.now().day
    f = datetime.now().year
    a = d
    b = e
    c = f - 3650

    url = "http://ichart.finance.yahoo.com/table.csv?s=" + stock + "&d=" + str(d) + "&e=" + str(e) + "&f=" + str(f) + \
    "&g=d&a=" + str(a) + "&b=" + str(b) + "&c=" + str(c) + "&ignore=.csv"

    rdata = request.urlopen(url)
    csv = rdata.read()
    # Save the string to a file
    csvstr = str(csv).strip("b'")
    lines = csvstr.split("\\n")
    filename = 'stockXls\\' + ticker + 'his.csv'
    f = open(filename, "w")
    for line in lines:
        f.write(line + "\n")
    f.close()

GetHistory("3481")

