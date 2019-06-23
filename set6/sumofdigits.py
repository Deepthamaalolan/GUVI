n=int(input())
sum1=0
while(n!=0):
    rem=n%10
    sum1=sum1+rem
    n=n/10
print(int(sum1))
