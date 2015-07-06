from yahoo_finance import Share 
from argparse import ArgumentParser
import time
import sys
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
sp500Price = ""
sp500Change = ""
sp500percentChange = ""
ndqChange = ""

def timeStamp():
	print "\n"
	global tsstart
	tsstart = time.time()
	st = datetime.datetime.fromtimestamp(tsstart).strftime('%Y-%m-%d %H:%M:%S')
	return st

def isMarketOpen():
#determines how many seconds after midnight now is, and compares it with the seconds after midnight in the blackout period.  Between 9am-9:45am Eastern Yahoo! sends N/A data for some fields, for which I don't have all of the error handling working
	newnow = datetime.datetime.now()
	midnight = datetime.datetime.combine(newnow.date(), datetime.time())
	seconds = (newnow - midnight).seconds
	#seconds = 33000
	startBlackout = 32400 #9:00am Eastern is 32,400 seconds after midnight, begin blackout period
	endBlackout = 35100 #9:34am Eastern is 35,100 seconds after midnight; end blackout period
	if (seconds >= startBlackout) and (seconds <= endBlackout):
		return 1
	else:
		return 0
	#sys.exit("that's all folks...")

def marketClosedReport():
	print "Between 9:00am - 9:45am Eastern (UTC-0:500) Yahoo Finance reports N/A values that are not handled; please re-run outside of blackout hours"

def runtimer_start():
	global starttime
	starttime = timeit.default_timer()

def runtimer_stop():
	stoptime = timeit.default_timer()
	runtime = stoptime - starttime
	print "Completed in: %s" % str(round(runtime, 2)), "seconds"

#function called getStock; expects 1 variable, returns the stock name from share class of the yahoo_finance module 
def getStock(self):
    return Share(self)

def getPrice(self):
	return self.get_price()

def percentChange(self):
	tickerPercentChange = (getDayChange(self)/getOpen(self)*100)
	return tickerPercentChange

def index_price():
	global sp500Change, sp500Price
	sp500Price = float(sp500index.get_price())
	sp500Open = float(sp500index.get_open())
	sp500Change = float(sp500index.get_change())
	global sp500percentChange
	sp500percentChange = ((sp500Change/sp500Open)*100)
	return (sp500Price, sp500Open, sp500Change, sp500percentChange)

def getOpen(self): 
	return float(self.get_open())

def getVolume(self):
	return float(self.get_volume())

def getAvgDailyVolume(self):
	return float(self.get_avg_daily_volume())

def getDayChange(self):
	#Checks to see if the gdc is None (e.g. between ~9am-9:45am Yhaoo Finance returns N/A for change).  If Yahoo-Finance returns N/A (none), then return 0 to prevent error.  Returning 0 causes winLoss() to return invalid data.
	gdc = mystock.get_change()
	if gdc is not None:
		#print ticker, gdc
		return float(self.get_change())
	else:
		return 0

def getDayHigh(self):
	return self.get_days_high()

def getDayLow(self):
	return self.get_days_low()

def getYearHigh(self):
	return self.get_year_high()

def getYearLow(self):
    return self.get_year_low()

def getinput():
	return raw_input("Ticker>")

def winList(self):
	if getDayChange(self) > 0:
		global winnerList
		winnerList += ticker

def looseList(self):
	if getDayChange(self) <= 0:
		global looserList
		looserList += ticker

def newHighTest(self):
	newhighpricetest = ""
	if getDayHigh(self) == getYearHigh(self):
		newhighpricetest = "yes"
		global yearhighlist
		yearhighlist += ticker
	else:
		newhighpricetest = "no"
	return newhighpricetest

def volumeHighTest(self):
	newvolumehightest = ""
	if getVolume(self) > getAvgDailyVolume(self):
		newvolumehightest = "yes"
		global volumealert
		volumealert += ticker 
	else:
		newvolumehightest = "no"
	return newvolumehightest

def newLowTest(self):
	newlowpricetest = ""
	if getDayLow(self) == getYearLow(self):
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
	if args.newlowFlag:
		print "Hitting 52-week low: \n" + yearlowlist

def yearHighSummary():
	#global yearhighlist
	if yearhighlist:
		print "\n", "Hitting 52-week high: \n" +  yearhighlist
	else:
		print "\n", "Hitting 52-week high: \n", "No tickers in watchlist hitting 52-week high \n"
		 

def detailTicker():
	#debug detail line item; modify so that -d fits the test case.
	if args.detail:
		#print ticker, myprice, myvolume, myavgdailyvolume, mydaychange, mydayhigh, mydaylow, myyearhigh, myyearlow, mynewhightest, myvolumehightest, mynewlowtest, myopen, mypercentchange
		tickerPrint = ticker.strip('\n')
		print tickerPrint, myprice, myopen, mydaychange, str(round(mypercentchange, 2))+'%'

def noInputError():
	print "Nothing specified, please run -h for help"

def noAction():
	print "\n", args.filename + ": " + "Watchlist triggered no alerts today."

def startup():
	print timeStamp()
	print "Running queries on " + numberOfLines + " symbols..."


def index_summary():
	print "S&P 500, Price: %s, Change: %s, Percent Change: %s" %(sp500Price, sp500Change, str(round(sp500percentChange,2))+'%'), "\n" #converts to string, and rounds my variable to 2 decimal places when printing

def outperformSP500(self):
	#tickerPrint = ticker.strip('\n')
	global sp500percentChange
	if mypercentchange > sp500percentChange:
		print ticker.strip('\n'), str(round(mypercentchange, 2))+'%'
 
parser = ArgumentParser(description = 'Watchlist Filtering for Yahoo-Finance')
parser.add_argument("-f", "--file", dest="filename", help="file name of watchlist; expects plain text file with 1 ticker symbol per line, and no empty lines at the end", metavar="FILE")
parser.add_argument("-v", "--volume", action="store_true", dest="volumeFlag", default=False, help="high volume notification")
parser.add_argument("-nl", "--low", action="store_true", dest="newlowFlag", default=False, help="new 52-week low notification")
parser.add_argument("-d", "--detail", action="store_true", dest="detail", default=False, help="detailed ticker info")
parser.add_argument("-wl", "--wins", action="store_true", dest="winnerlist", default=False, help="outputs today's winners")
parser.add_argument("-ll", "--losses", action="store_true", dest="looserlist", default=False, help="outputs today's loosers")
parser.add_argument("-ip", "--indexprices", action="store_true", dest="indexprices", default=False, help="outputs current index prices")
parser.add_argument("-op", "--outperformance", action="store_true", dest="outperformance", default=False, help="prints tickers symbol and change info if ticker is outperformaning the day's S&P 500 performance.  MUST USE WITH -ip")
parser.add_argument("-nh", "--newhighs", action="store_true", dest="newhighs", default=False, help="prints tickers from watchlist hitting new 52 week highs")

args = parser.parse_args()

mymarketstatus = isMarketOpen()
#mymarketstatus = 1 #debugging condition

if mymarketstatus < 1:
	if args.filename:
		runtimer_start()
		watchList = open(args.filename)
		ticker = watchList.readlines()
		numberOfLines = str(len(ticker))
		startup()
		if args.indexprices:
			indexinfo = index_price()
			index_summary()

		for ticker in ticker:
			mystock = getStock(ticker)
			myprice = getPrice(mystock)
			myopen = getOpen(mystock)
			myvolume = getVolume(mystock)
			myavgdailyvolume = getAvgDailyVolume(mystock)
			mydaychange = getDayChange(mystock)
			mydayhigh = getDayHigh(mystock)
			mydaylow = getDayLow(mystock)
			if args.newhighs:
				myyearhigh = getYearHigh(mystock) 
			myyearlow = getYearLow(mystock)
			mynewhightest = newHighTest(mystock)
			myvolumehightest = volumeHighTest(mystock)
			mynewlowtest = newLowTest(mystock)
			mypercentchange = percentChange(mystock)
			winList(mystock)
			looseList(mystock)
			detailTicker()
			if args.outperformance:
				outperformSP500(mystock)
	if args.filename:
		if args.newhighs:
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
else:
	marketClosedReport()
