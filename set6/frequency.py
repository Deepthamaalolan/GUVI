m,n=map(int,input().split())
count=0
s=list(map(int,input().split()))[:m]
for i in range(0,m):
    if s[i]==n:
        count=count+1 
print(count)
