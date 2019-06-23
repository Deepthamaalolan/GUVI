m,n=map(int,input().split())
s=list(map(int,input().split()))[:m]
for i in range(0,m):
    if s[i]==n:
        print("yes")
