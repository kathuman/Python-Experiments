# Examples of output formatting

from datetime import datetime

def main():   
    now = datetime.now()
    ## date Formatting##
    # %y/%Y-year formatting, %a/%A - weekday, %b/%B - Month, %d - day of the month
    
    print(now.strftime("%Y"))
    print(now.strftime("%A, %d %B, %Y"))
    
    ## formatting adjusted to the local appropriate formatting (as used in the computer that us running it.
    print(now.strftime("%c"))
    print(now.strftime("%x"))
    print(now.strftime("%X"))
    
    ## time formatting ##
    # %I/%H -12/12H, %M - minute, %S -second, %p - locale's AM/PM
    print(now.strftime("%I:%M:%S %p"))
    print(now.strftime("%H:%M"))

if __name__ == "__main__":
    main()