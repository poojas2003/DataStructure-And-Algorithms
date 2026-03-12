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
