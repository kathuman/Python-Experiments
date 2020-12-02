def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x = x + increment

def mainfrange():
    for n in frange(0, 4, 0.5):
        print(n)
        
########################################
        
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

def maincountdown():
    c=countdown(3)
    while c<=0:
        print(c)
    next(c)

if __name__=="__main__":
#    mainfrange()
        countdown(3)
