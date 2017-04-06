# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  




date_start = '01-02-2013'    
date_stop = '07-28-2015'


from datetime import date
from datetime import datetime
def days_between(start, stop):

    startYear = int(start[6:])
    endYear = int(stop[6:])
    startDay = int(start[3:5])
    endDay = int(stop[3:5])
    startMonth = int(start[0:2])
    endMonth = int(stop[0:2])
    
    begin = date(startYear, startMonth, startDay)
    end = date(endYear, endMonth, endDay)
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
        elif (startMonth > 7): 
           days -= 1
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
    startYear = int(start[6:])
    endYear = int(stop[6:])
    startDay = int(start[3:5])
    endDay = int(stop[3:5])
    startMonth = int(start[0:2])
    endMonth = int(stop[0:2])
    
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


