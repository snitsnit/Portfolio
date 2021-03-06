#Jeremiah Dir
#jdir@gatech.edu
#I completed this assignment alone, using only this course's resources

from urllib import request
import csv
import time
import datetime
def webScraper():
    #baseUrl = 'http://www.nasdaq.com/symbol'
    #response = request.urlopen(baseURl)
    #theBytes = response.read()
    #theHtml = theBytes.decode()
    file1 = open('stockData.csv','w')
    CSVWriter = csv.writer(file1)
    CSVWriter.writerow(['Timestamp','Company','Daily High','Daily Low','Share Volume','Average Share','Annual Target'])
    file1.close()
    while True:
        file2 = open('stockData.csv','a')
        CSVWriter2 = csv.writer(file2)
        compSymbols = ['CHKE','int','sum','gas','sun']
        symbolInfo = []
        totalValues = []
        for symbol in compSymbols:
            values = []
            url = 'http://www.nasdaq.com/symbol/' + symbol
            #print ( url )
            response = request.urlopen(url)
            theHtml2 = response.read().decode()

            dailyHighPos = theHtml2.index('Label3') + 15
            dailyHigh = theHtml2[dailyHighPos:dailyHighPos+5]

            dailyLowPos = theHtml2.index('Label1') + 15
            dailyLow = theHtml2[dailyLowPos:dailyLowPos+5]

            shareVolumePos = theHtml2.index(symbol.upper() + '_Volume') + 13
            shareVolume = theHtml2[shareVolumePos:shareVolumePos+6]

            avgSharePos = theHtml2.index('Annualized dividend')+94
            avgShare = theHtml2[avgSharePos:avgSharePos+6]
            avgShareF = ''

            for char in avgShare:
                if char in ['0','1','2','3','4','5','6','7','8','9','0','.']:
                    avgShareF += char

            if symbol == 'sum':
                avgSharePos = theHtml2.index('Annualized dividend') + 87
                avgShareF = theHtml2[avgSharePos:avgSharePos+3]

            oneYearTargetPos = theHtml2.index('1 Year Target')+81
            oneYearTarget = theHtml2[oneYearTargetPos:oneYearTargetPos+6]
            oneYearTargetF = ''

            for char in oneYearTarget:
                if char in ['0','1','2','3','4','5','6','7','8','9','0','.']:
                    oneYearTargetF += char
            dt = time.time()
            st = datetime.datetime.fromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')
            values.append(st)
            values.append(symbol)
            values.append(dailyHigh)
            values.append(dailyLow)
            values.append(shareVolume)
            values.append(avgShareF)
            values.append(oneYearTargetF)
            totalValues.append(values)
            #print ( values )

        #print ( totalValues)
        for item in totalValues:
            CSVWriter2.writerow(item)
        #print ( 'Added a row!')
        time.sleep(3000)





webScraper()
