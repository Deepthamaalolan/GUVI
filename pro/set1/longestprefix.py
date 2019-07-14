def common(str1, str2): 
    len1 = len(str1) 
    len2 = len(str2) 
      
    result = "" 
      
    # Compare str1 and str2 
    j = 0
    i = 0
    while(i <= len1 - 1 and j <= len2 - 1): 
        if (str1[i] != str2[j]): 
            break
        result += (str1[i]) 
          
        i += 1
        j += 1
  
    return (result) 
  
# A Function that returns the longest  
# common prefix from the array of strings 
def commonPrefix(arr, n): 
      
    # sorts the N set of strings 
    arr.sort(reverse = False) 
  
    # prints the common prefix of the first  
    # and the last string of the set of strings 
    print(common(arr[0], arr[n - 1])) 
  
# Driver Code 
if __name__ == '__main__': 
    T=int(input())
    l=[]
    for i in range(0,T):
        x=input()
        l.append(x)
    n = len(l) 
  
    commonPrefix(l, n) 
