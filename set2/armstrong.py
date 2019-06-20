num = int(input())  
sum1 = 0  
temp = num  
  
while temp > 0:  
   rem = temp % 10  
   sum1+= rem** 3  
   temp //= 10  
  
if num == sum1:  
   print("YES")  
else:  
   print("NO") 
