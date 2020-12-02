# example of working with date and time

from datetime import date
from datetime import time
from datetime import datetime

def main():
    
    today = date.today()
#    print("Today's date is ", today)
#    print("Date Components: ",today.day,today.month,today.year)
    
#    print("Today's weekday number is: ", today.weekday())
    
#    today = datetime.now()
#    print("The current date and time is: ", today)
    
#    t = datetime.time(datetime.now())
#    print("The current time is: ", t)
 
    wd = date.weekday(today)
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print("Today is day number %d" % wd)
    print("which is a " + days[wd])
    
if __name__ == "__main__":
    main()