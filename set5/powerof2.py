n=int(input())
if(n>0):
    while(n%2 == 0):
        n/=2
        if(n == 1):
            print("yes")
    if(n == 0 or n != 1):
        print("no")
