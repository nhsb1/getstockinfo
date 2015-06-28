from yahoo_finance import Share 
#from sys import argv
from argparse import ArgumentParser

mystock = ""
yearhighlist = ""
yearlowlist = ""
volumealert = ""

def getStock(stock):
    return Share(ticker)

def getPrice(stock):
	return mystock.get_price()

def getVolume(stock):
	return float(mystock.get_volume())

def getAvgDailyVolume(stock):
	return float(mystock.get_avg_daily_volume())

def getDayChange(stock):
	return float(mystock.get_change())

def getDayHigh(stock):
	return mystock.get_days_high()

def getDayLow(stock):
	return mystock.get_days_low()

def getYearHigh(stock):
	return mystock.get_year_high()

def getYearLow(stock):
    return mystock.get_year_low()

def getinput(stock):
	return raw_input("Ticker>")

def newHighTest(stock):
	newhighpricetest = ""
	if getDayHigh(stock) == getYearHigh(stock):
		newhighpricetest = "yes"
		global yearhighlist
		yearhighlist += ticker
	else:
		newhighpricetest = "no"
	return newhighpricetest

def volumeHighTest(stock):
	newvolumehightest = ""
	if getVolume(stock) > getAvgDailyVolume(stock):
		newvolumehightest = "yes"
		global volumealert
		volumealert += ticker 
	else:
		newvolumehightest = "no"
	return newvolumehightest

def newLowTest(stock):
	newlowpricetest = ""
	if getDayLow(stock) == getYearLow(stock):
		newlowpricetest = "yes"
		global yearlowlist
		yearlowlist += ticker
	else:
		newlowpricetest = "no"
	return newlowpricetest

def volumeSummary():
	if args.volumeFlag:
		print "High Volume alert: \n" + volumealert

def yearLowSummary():
	if args.lowVolumeFlag:
		print "Hitting 52-week low: \n" + yearlowlist

def yearHighSummary():
	print "Hitting 52-week high: \n" +  yearhighlist

def detailTicker():
	if args.detail:
		print ticker, myprice, myvolume, myavgdailyvolume, mydaychange, mydayhigh, mydaylow, myyearhigh, myyearlow, mynewhightest, myvolumehightest, mynewlowtest

def noInputError():
	print "Nothing specified, plus run -h for help"

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename", help="file to open", metavar="FILE")
parser.add_argument("-v", "--volume", action="store_true", dest="volumeFlag", default=False, help="high volume notification")
parser.add_argument("-l", "--low", action="store_true", dest="lowVolumeFlag", default=False, help="low volume notification")
parser.add_argument("-d", "--detail", action="store_true", dest="detail", default=False, help="detailed ticker info")
args = parser.parse_args()

if args.filename:
	watchList = open(args.filename)
	ticker = watchList.readlines()
	numberOfLines = str(len(ticker))
	print "Running queries on " + numberOfLines + " symbols..."

	for ticker in ticker:
		mystock = getStock(ticker)
		myprice = getPrice(mystock)
		myvolume = getVolume(mystock)
		myavgdailyvolume = getAvgDailyVolume(mystock)
		mydaychange = getDayChange(mystock)
		mydayhigh = getDayHigh(mystock)
		mydaylow = getDayLow(mystock)
		myyearhigh = getYearHigh(mystock)
		myyearlow = getYearLow(mystock)
		mynewhightest = newHighTest(mystock)
		myvolumehightest = volumeHighTest(mystock)
		mynewlowtest = newLowTest(mystock)
		detailTicker()

if args.filename:
	yearHighSummary()
	yearLowSummary()
	volumeSummary()
else:
	noInputError()

