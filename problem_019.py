'''


You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
weekday = 2
monthday = 1
day = 1
month = 1
year = 1900

firstsundays = 0 

def getStrWkDay(day):
    if day == 1: 
        return 'Sunday'
    elif day == 2:
        return 'Monday'
    elif day == 3:
        return 'Tuesday'
    elif day == 4:
        return 'Wednesday'
    elif day == 5:
        return 'Thursday'
    elif day == 6:
        return 'Friday'
    elif day == 0:
        return 'Saturday'
    else: return 'Error'

def getStrMonth(month):
    if month == 1:
        return 'January'
    elif month == 2:
        return 'February'
    elif month == 3:
        return 'March'
    elif month == 4:
        return 'April'
    elif month == 5:
        return 'May'
    elif month == 6:
        return 'June'
    elif month == 7:
        return 'July'
    elif month == 8:
        return 'August'
    elif month == 9:
        return 'September'
    elif month == 10:
        return 'October'
    elif month == 11:
        return 'November'
    elif month == 12:
        return 'December'
    else: return 'Error'


while True:

    # if day >= 1 and day < 10:
    #     print('Today is {}, {} {}, {}'.format(getStrWkDay((day+1)%7),getStrMonth(month),monthday,year))

    if monthday == 1 and  getStrWkDay(weekday%7)=='Sunday' and year > 1900:
        firstsundays +=1

    day += 1
    monthday += 1
    weekday += 1
    
    if month in [4,6,9,11] and monthday == 31:
        monthday = 1
        month +=1

    elif month in [1,3,5,7,8,10] and monthday == 32:
        monthday = 1
        month += 1

    elif month == 12 and monthday == 32:
        year += 1
        monthday = 1
        month = 1

    elif month == 2 and year % 400 == 0:
        if monthday == 30:
            monthday = 1
            month += 1
    
    elif month == 2 and year % 100 == 0 and year % 400 != 0:
        if monthday == 29:
            monthday = 1
            month += 1

    elif month == 2 and year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
        if monthday == 30:
            monthday = 1
            month += 1
    
    elif month == 2 and year % 4 != 0 and year % 100 != 0 and year % 400 != 0:
        if monthday == 29:
            monthday = 1
            month += 1
    
    #else: continue
    #if day == 35: break
    if day == 36891: break
print('There were {} first Sundays in the 20th Century'.format(firstsundays))