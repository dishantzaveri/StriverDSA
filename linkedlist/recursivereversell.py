class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, head):
         if head is None or head.next is None:
             return head
         newHead=self.reverseList(head.next)
         front=head.next
         front.next=head
         head.next=None
         return newHead
             

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    sol = Solution()
    reversed_head = sol.reverseList(head)
    while reversed_head:
        print(reversed_head.val, end=" ")
        reversed_head = reversed_head.next