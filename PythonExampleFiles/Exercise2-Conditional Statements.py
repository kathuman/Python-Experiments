# examples with conditional statements

def main():
    x,y = 100,1000

## first form of conditional statement
#    if(x < y):
#        st = "x is less than y"
#    elif (x==y):
#        st = "x is equal to y"
#    else:
#        st = "x is greater than y"

    st = "x is smaller than y" if (x < y) else "x is greater or equal to y"
    print(st)

if __name__ == "__main__":
    main()
