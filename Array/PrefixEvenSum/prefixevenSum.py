#even prefix sum

A=[1,2,3,4,5]
even_prefix=[0]*len(A)
even_prefix[0]=A[0]
for i in range(1,len(A)):
    if i%2==0:
        even_prefix[i]=even_prefix[i-1]+A[i]
    else:
        even_prefix[i]=even_prefix[i-1]
        
print(even_prefix) 
