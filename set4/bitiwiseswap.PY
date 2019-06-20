a=int(input())
b=int(input())
print(a,b ,end=" ")
print("\n")
a = a ^ b;
b = a ^ b;
a = a ^ b;
    
print(a,b,end=" ")
