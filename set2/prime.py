d=int(input())
flag=0
if d>1:
    for i in range(2,d):
        if d%i ==0:
            flag=1
    if flag==0:
        print("yes")
    else :
        print("no")
else:
    print("no")
