# Example in the EDX python course regardng tuples and objects in Python
def FindDivisors(n1,n2):
    divisors = ()
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            divisors = divisors + (i,)
    return divisors

if __name__=="__main__":
    n1 = int(raw_input("Enter the first Number: "))
    n2 = int(raw_input("Enter the second number: "))
    print("The common divisors for "+ str(n1) + " and " + str(n2) + " are: " + str(FindDivisors(n1,n2))) 