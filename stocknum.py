#-*-coding:UTF-8-*-
import re
import urllib2,urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 取得股票代號及名稱(只包含基本代號)
def getStockNumberAndName(index):
    try:
        url = 'http://www.twse.com.tw/ch/trading/inc/STKCHOICE/STK%02d.php?STK=%02d'%(index,index)
        #設定網址 為 STK01..23.php?STK=01 ... 23
        req = urllib2.Request(url)
        # 建立一個 GET 的request
        rawData = urllib2.urlopen(req)
        #實際 request 網誌
        tmpData = rawData.read()
        # 將資料讀取出來
        tmp = re.findall(u"<span class='basic2'>(\d{4})&nbsp;(.*)</span>",tmpData)
        #透過 regular expression 抓取股票代號 和名字 目前只判斷4位數字代號(有些特殊股票代號請自行嘗試)
        return tmp;
        #回傳找到的結果 findall 找到的結果會是一個 Array

    except Exception , e:
        print e
        # 有錯的話印出來

# 取得全部股票代號及名稱
def getAllStockNumberAndName():
    try:
        result = []
        for index in range(1,24): #目前股票分類只有23個項目
            tmpResult = getStockNumberAndName(index)
            if(tmpResult): #有資料就加總 例如:19是空的
                result += tmpResult
                #把資料合併起來
        return result

        #回傳結果
    except Exception , e:
        print e


stockNumAndName = getAllStockNumberAndName()
#print stockNumAndName

for oneSet in stockNumAndName:
    print oneSet[0] + oneSet[1]