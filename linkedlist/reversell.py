class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self,head):
        prev=None
        temp=head
        while temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev
    
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
newHead = sol.reverseList(head)
printList(newHead)