numbers=['one','two','three','four','five','six','seven','eight','nine','ten']
n=int(input())
for i in range(1,10):
    if i==n:
        print(numbers[i-1])
