from yahoo_finance import Share 

#initalizes mystock variable as empty
mystock = ""

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
		#print newhightest, getDayHigh, getYearHigh
	else:
		newhighpricetest = "no"
		#print newhightest, getDayHigh, getYearHigh
	return newhighpricetest

def volumeHighTest(stock):
	newvolumehightest = ""
	if getVolume(stock) > getAvgDailyVolume(stock):
		newvolumehightest = "yes"
	else:
		newvolumehightest = "no"
	return newvolumehightest

def newLowTest(stock):
	newlowpricetest = ""
	if getDayLow(stock) == getYearLow(stock):
		newlowpricetest = "yes"
	else:
		newlowpricetest = "no"
	return newlowpricetest


ticker = getinput(mystock)
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

print ticker, myprice, myvolume, myavgdailyvolume, mydaychange, mydayhigh, mydaylow, myyearhigh, myyearlow, mynewhightest, myvolumehightest, mynewlowtest
