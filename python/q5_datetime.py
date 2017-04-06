date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  

from datetime import date
from datetime import datetime

def convert_month(month):

    return{
        'Jan' : 1,
        'Feb' : 2,
        'Mar' : 3,
        'Apr' : 4,
        'May' : 5,
        'Jun' : 6,
        'Jul' : 7,
        'Aug' : 8,
        'Sep' : 9, 
        'Oct' : 10,
        'Nov' : 11,
        'Dec' : 12
    }[month]

def convert_date(date):
    
    if len(date) < 10:
        year = int(date[4:])
        day = int(date[2:4])
        month = int(date[0:2])
    elif len(date) > 10:
        year = int(date[7:])
        day = int(date[0:2])
        month = convert_month(date[3:6])
    else:
        year = int(date[6:])
        day = int(date[3:5])
        month = int(date[0:2])
    
    return (year, month, day)

def days_between(start, stop):

    startDate = convert_date (start)
    endDate = convert_date(stop)
    
    begin = date(*startDate)
    end = date(*endDate)
    print (abs((end-begin).days))
    return (abs(end-begin).days)

def days_left_in_year (month, day):
    startMonth = month
    startDay = day
    days = 0
    
    if (startMonth%2 == 0):
        days += (30 - startDay)
        days += (12- startMonth)/2*61 +1
        if (startMonth == 2):
           days -= 2
        else: 
           pass
    else:
        days += (31 - startDay)
        days += (11 - startMonth)/2 * 61 +31
        if (startMonth == 1):
            days -= 2
        else:
            pass
        
    return days


def days_in_between(start, stop):
#does not take into account leap years

    startDate = convert_date (start)
    endDate = convert_date(stop)
    
    startYear = startDate[0]
    endYear = endDate[0]
    
    startMonth = startDate[1]
    endMonth = endDate[1]
    
    startDay = startDate[2]
    endDay = endDate[2]
    
    days = 0

    days += days_left_in_year(startMonth, startDay)
    days += (365 - days_left_in_year(endMonth, endDay))
             
    if (endYear != startYear):
        days += ((endYear - startYear) - 1)*365
    else: 
        pass
    
    print (days)
    return days

days_between(date_start, date_stop)
days_in_between(date_start, date_stop)


