from yahoo_finance import Share 
from argparse import ArgumentParser
import time
import datetime

mystock = ""
yearhighlist = ""
yearlowlist = ""
volumealert = ""
winnerList = ""
looserList = ""
tsstart = ""

def getStock(stock):
    return Share(ticker)

def getPrice(stock):
	return mystock.get_price()

def getVolume(stock):
	return float(mystock.get_volume())

def getAvgDailyVolume(stock):
	return float(mystock.get_avg_daily_volume())

def getDayChange(stock):
	#Checks to see if the gdc is None (e.g. between ~9am-9:45am Yhaoo Finance returns N/A for change).  If Yahoo-Finance returns N/A (none), then return 0 to prevent error.  Returning 0 causes winLoss() to return invalid data.
	gdc = mystock.get_change()
	if gdc is not None:
		print ticker, gdc
		return float(mystock.get_change())
	else:
		return 0

def getDayHigh(stock):
	return mystock.get_days_high()

def getDayLow(stock):
	return mystock.get_days_low()

def getYearHigh(stock):
	return mystock.get_year_high()

def getYearLow(stock):
    return mystock.get_year_low()

def getinput():
	return raw_input("Ticker>")

def winLossList(stock):
	if getDayChange(stock) > 0:
		global winnerList
		winnerList += ticker
	else:
		global looserList
		looserList += ticker

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

def winLossReport():
	print "\n"
	print "Winners: \n", winnerList
	print "Loosers: \n", looserList


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
	print "Nothing specified, please run -h for help"

def noAction():
	print "\n", args.filename + ": " + "Watchlist triggered no alerts today."

def timeStamp():
	global tsstart
	tsstart = time.time()
	st = datetime.datetime.fromtimestamp(tsstart).strftime('%Y-%m-%d %H:%M:%S')
	return st

def timeStop():
	tsstop = time.time()
	print tsstart
	print tsstop
	st = datetime.datetime.fromtimestamp(tsstop).strftime('%Y-%m-%d %H:%M:%S')
	#global tsstart
	#timestop = tsstart - tsstop
	#print timeStop

def startup():
	print timeStamp()
	print "Running queries on " + numberOfLines + " symbols..."
 
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename", help="file name of watchlist; expects plain text file with 1 ticker symbol per line, and no empty lines at the end", metavar="FILE")
parser.add_argument("-v", "--volume", action="store_true", dest="volumeFlag", default=False, help="high volume notification")
parser.add_argument("-l", "--low", action="store_true", dest="lowVolumeFlag", default=False, help="low volume notification")
parser.add_argument("-d", "--detail", action="store_true", dest="detail", default=False, help="detailed ticker info")
parser.add_argument("-wl", "--winLoss", action="store_true", dest="winnerlooserlist", default=False, help="outputs today's winners & loosers")
args = parser.parse_args()

if args.filename:
	watchList = open(args.filename)
	ticker = watchList.readlines()
	numberOfLines = str(len(ticker))
	startup()

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
		winLossList(mystock)
		detailTicker()

if args.filename:
	#global yearhighlist
	if yearhighlist:
		yearHighSummary()
	if yearlowlist:
		yearLowSummary()
	if volumealert:
		volumeSummary()
	if args.winnerlooserlist:
		winLossReport()
	timeStop()
else:
	noInputError()

