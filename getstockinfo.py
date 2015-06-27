from yahoo_finance import Share 
from sys import argv
script, filename = argv

#initalizes mystock variable as empty
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

#def argsParser(options): 
#	parser = ArgumentParser()
#	parser.add_argument("-f", "--file", dest="filename", help="file to open", metavar="FILE")
#	parser.add_argument("-v", "--volume", ction="store_true", dest="volumeFlag", default=False, help="high volume notification")
#	parser.add_argument("-l", "--52weeklow", action="store_true", dest="YearLow", default=False, help="52-week low notification")
#	args = parser.parse_args()
#	if args.filename:
#		watchList = open(args.filename)
#		ticker = watchList.readlines()
#		numberOfLines = str(len(stock))
#		print ticker
#	return ticker



watchList = open(filename)
ticker = watchList.readlines()
numberOfLines = str(len(ticker))


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
	#print ticker, myprice, myvolume, myavgdailyvolume, mydaychange, mydayhigh, mydaylow, myyearhigh, myyearlow, mynewhightest, myvolumehightest, mynewlowtest

print "Hitting 52-week high: " + yearhighlist
print "Hitting 52-week low: " + yearlowlist
print "High Volume alert: " + volumealert
