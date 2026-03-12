A=[1,2,3,4,5,6,-1]
K=4
n=len(A)
start=0
end=K-1

result=float('-inf')

while(end<n):
    subArraySum=0
    for i in range(start,end+1):
        subArraySum+=A[i]
    result=max(subArraySum,result)
    start+=1
    end+=1
        
print(result);

//Time Complexity---O(n)
A=[1,2,3,4,5,6,-1]
k=4
n=len(A)

window_sum=sum(A[0:k])
max_sum=window_sum

for i in range(k,n):
    window_sum=window_sum+A[i]-A[i-k]
    max_sum=max(window_sum,max_sum)
    
print(max_sum)    
    
