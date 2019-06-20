d=int(input())
l=[]
k=int(input())
for i in range(0,d):
    n=int(input())
    l.append(n)
sum1=0
for i in range(0,k):
    sum1=sum1+l[i]
print(int(sum1))
