from yahoo_finance import Share 
from argparse import ArgumentParser
import time
import datetime
import timeit

mystock = ""
yearhighlist = ""
yearlowlist = ""
volumealert = ""
winnerList = ""
looserList = ""
starttime = ""
sp500index = Share('^GSPC') 
nasdaqindex = Share('^IXIC')
sp500Change = ""
ndqChange = ""

def runtimer_start():
	global starttime
	starttime = timeit.default_timer()

def runtimer_stop():
	stoptime = timeit.default_timer()
	runtime = stoptime - starttime
	print "Completed in: %s" % runtime, "seconds"

def getStock(stock):
    return Share(ticker)

def getPrice(stock):
	return mystock.get_price()

def percentChange(stock):
	tickerPercentChange = (getDayChange(stock)/getOpen(stock)*100)
	return tickerPercentChange

def index_price(stock):
	
	sp500symbol = "^GSPC"
	sp500Price = float(sp500index.get_price())
	sp500Open = float(sp500index.get_open())
	sp500Change = float(sp500index.get_change())
	sp500percentChange = ((sp500Change/sp500Open)*100)

	print sp500symbol
	print sp500Price
	print sp500Open
	print sp500percentChange

def getOpen(stock): 
	return float(mystock.get_open())

def getVolume(stock):
	return float(mystock.get_volume())

def getAvgDailyVolume(stock):
	return float(mystock.get_avg_daily_volume())

def getDayChange(stock):
	#Checks to see if the gdc is None (e.g. between ~9am-9:45am Yhaoo Finance returns N/A for change).  If Yahoo-Finance returns N/A (none), then return 0 to prevent error.  Returning 0 causes winLoss() to return invalid data.
	gdc = mystock.get_change()
	if gdc is not None:
		#print ticker, gdc
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

def winList(stock):
	if getDayChange(stock) > 0:
		global winnerList
		winnerList += ticker

def looseList(stock):
	if getDayChange(stock) <= 0:
		global looserList
		looserList += ticker

def newHighTest(stock):
	newhighpricetest = ""
	if getDayHigh(stock) == getYearHigh(stock):
		newhighpricetest = "yes"
		global yearhighlist
		yearhighlist += ticker
		#print ticker, myprice
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

def winReport():
	print "\n", "Winners: \n", winnerList

def lossReport():
	print "\n", "Loosers: \n", looserList

def volumeSummary():
	if args.volumeFlag:
		print "\n", "High Volume alert: \n" + volumealert

def yearLowSummary():
	if args.lowVolumeFlag:
		print "Hitting 52-week low: \n" + yearlowlist

def yearHighSummary():
	print "\n", "Hitting 52-week high: \n" +  yearhighlist

def detailTicker():
	#debug detail
	if args.detail:
		#print ticker, myprice, myvolume, myavgdailyvolume, mydaychange, mydayhigh, mydaylow, myyearhigh, myyearlow, mynewhightest, myvolumehightest, mynewlowtest, myopen, mypercentchange
		print ticker, myprice, myopen, mydaychange, mypercentchange

def noInputError():
	print "Nothing specified, please run -h for help"

def noAction():
	print "\n", args.filename + ": " + "Watchlist triggered no alerts today."

def timeStamp():
	print "\n"
	global tsstart
	tsstart = time.time()
	st = datetime.datetime.fromtimestamp(tsstart).strftime('%Y-%m-%d %H:%M:%S')
	return st

def startup():
	print timeStamp()
	print "Running queries on " + numberOfLines + " symbols..."


 
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename", help="file name of watchlist; expects plain text file with 1 ticker symbol per line, and no empty lines at the end", metavar="FILE")
parser.add_argument("-v", "--volume", action="store_true", dest="volumeFlag", default=False, help="high volume notification")
parser.add_argument("-l", "--low", action="store_true", dest="lowVolumeFlag", default=False, help="low volume notification")
parser.add_argument("-d", "--detail", action="store_true", dest="detail", default=False, help="detailed ticker info")
parser.add_argument("-wl", "--wins", action="store_true", dest="winnerlist", default=False, help="outputs today's winners")
parser.add_argument("-ll", "--looses", action="store_true", dest="looserlist", default=False, help="outputs today's loosers")
parser.add_argument("-ip", "--indexprices", action="store_true", dest="indexprices", default=False, help="outputs current index prices")

args = parser.parse_args()

if args.filename:
	runtimer_start()
	watchList = open(args.filename)
	ticker = watchList.readlines()
	numberOfLines = str(len(ticker))
	startup()

	for ticker in ticker:
		mystock = getStock(ticker)
		myprice = getPrice(mystock)
		myopen = getOpen(mystock)
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
		mypercentchange = percentChange(mystock)
		winList(mystock)
		looseList(mystock)
		detailTicker()

if args.filename:
	#global yearhighlist
	if args.indexprices:
		index_price('^IXIC')
	if yearhighlist:
		yearHighSummary()
	if yearlowlist:
		yearLowSummary()
	if volumealert:
		volumeSummary()
	if args.winnerlist:
		winReport()
	if args.looserlist:
		lossReport()
	#else: #if no yearhigh/low/volume, then print no action
	#	noAction()
	runtimer_stop()
else:
	noInputError()
