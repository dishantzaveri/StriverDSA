
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

class Solution:
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None
        slow = head
        fast = head.next.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head

def printLL(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original Linked List:", end=" ")
    printLL(head)

    obj = Solution()
    head = obj.deleteMiddle(head)

    print("Updated Linked List:", end=" ")
    printLL(head)
