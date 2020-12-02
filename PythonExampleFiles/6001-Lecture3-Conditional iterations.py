# Simple code to calculate the square of a value through iterations
def Exercise1():
    x=6
    ans=0
    itersLeft =x
    while itersLeft !=0:
        ans=ans+x
        itersLeft = itersLeft-1
    print(str(x) + "*"+str(x)+"="+str(ans))

def Exercise2():    
    num=0
    while num<=5:
        print num
        num +=1
    print "Outside of loop"
    print num
    
def Exercise3():
    # Find the cube root of a perfect cube
    # This is called a guess and check model
    x = int(raw_input("Enter an positive integer: "))
    ans=0
    while ans**3<x:
        ans = ans +1
    if ans**3 != x:
       print(str(x)+" is not a perfect cube")
    else:
        print("cube root of "+str(x)+" is "+str(ans))

def Primes2():
    MaxNum = int(raw_input("What is the maximum number you want to explore? : "))
    myList = [1]
    for n in range(2, MaxNum):
        for x in range(2, n):
            if n % x == 0:
                #print n, 'equals', x, '*', n/x
                break
        else:
         # loop fell through without finding a factor
            #print n, 'is a prime number'
            myList.append(n)
    print("Statistics")
    print("Number of Primes: " + str(len(myList)))
    print("Largest Prime found: " + str(myList[len(myList)-1]))
    print("Prime List: " + str(myList))   
            
Primes2()