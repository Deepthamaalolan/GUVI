start =int(input())
end = int(input())
  
for i in range(start, end + 1): 
      
   # If num is divisible by any number   
   # between 2 and val, it is not prime  
   if i > 1: 
       for n in range(2, i): 
           if (i % n) == 0: 
               break
       else: 
           print(i) 
    
