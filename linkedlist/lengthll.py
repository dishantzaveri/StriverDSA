class Node:
    def __init__(self,data1):
        self.data=data1
        self.next= None
        
class Solution:
    def lengthOfLinkedList(self,head):
        count =0
        temp=head
        while temp is not None:
            count+=1
            temp=temp.next
        return count
        
if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    # head.next.next = Node(30)
    obj = Solution()

    print("Length of Linked List:",
          obj.lengthOfLinkedList(head))