class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class Solution:
    #self--->this A--->head in java
    def printNode(self,A):
        curr=A
        values=[]
        #current!=null in java
        while(curr):
            values.append(str(curr.val))
            curr=curr.next
        print(" ".join(values)+" ")
            
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)

solution=Solution()
solution.printNode(head)

Time Complexity:O(N)
Space Complexity:O(N)

#you can create your own list using make_list 

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
def make_list(vales):
  if not vales: return None
  head=Node(vales[0])
  cur=head
  for V in vales[1:]:
    cur.next=Node(V)
    cur=cur.next
  return head

class Solution:
    #self--->this A--->head in java
    def printNode(self,A):
        curr=A
        values=[]
        #current!=null in java
        while(curr):
            values.append(str(curr.val))
            curr=curr.next
        print(" ".join(values)+" ")
            
head=make_list([1,2,3])

solution=Solution()
solution.printNode(head)



