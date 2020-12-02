def Prog1():
    x = int(input("Enter a Number: "))
    if (x%2==0):
        print("")
        print("Even")
    else:
        print("")
        print("Odd")
    print("Done with Conditional")

def Prog2():
    x = int(input("Enter a Number: "))
    if x%2==0:
        if x%3==0:
            print("divisible by 2 and 3")
        else:
            print("divisible by 2 and NOT by 3")
    elif x%3==0:
        print("divisible by 3")
    else:
        print("not divisible by 2 or 3")
    print("done with conditionals")

Prog2()
