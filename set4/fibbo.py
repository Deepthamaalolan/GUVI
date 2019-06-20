n=int(input())
b=1
a=0
print(b,end=" ")
for i in range(1,n+1):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
