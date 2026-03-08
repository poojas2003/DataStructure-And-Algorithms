
def solve(A):
    n=len(A);
    prefix_even=[0]*(n+1);
    prefix_odd=[0]*(n+1);
    for i in range(n):
        prefix_even[i+1] = prefix_even[i] + (A[i] if i%2 == 0 else 0)
        prefix_odd[i+1] = prefix_odd[i] + (A[i] if i%2 == 1 else 0)
    total_even=prefix_even[n]
    total_odd=prefix_odd[n]
    count=0
    for i in range(n):
        left_even=prefix_even[i]
        left_odd=prefix_odd[i]
        right_even=total_even-prefix_even[i+1]
        right_odd=total_odd-prefix_odd[i+1]
        new_even=left_even+right_odd
        new_odd=left_odd+right_even
            
        if new_even==new_odd:
            count += 1
            
    return count
        
A = [2,1,6,4]
result=solve(A)
print('result',result)
        
        
    
