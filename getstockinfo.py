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

print ticker, myprice, myvolume, myavgdailyvolume, mydaychange, mydayhigh, mydaylow, myyearhigh, myyearlow




