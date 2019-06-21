a=int(input())
numbers = list(map(int, input().split()))[:a]
print(min(numbers),max(numbers),end=" ")
