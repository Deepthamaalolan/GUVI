a = int(input())
b=int(input())

  
for num in range(a,b+1) :
    sum1=0
    temp=num
    while temp > 0:  
        rem = temp % 10  
        sum1+= rem** 3  
        temp //= 10  
  
    if num == sum1:  
        print(num)  
   
