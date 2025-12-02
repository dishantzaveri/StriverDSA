
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def append(self, head, value):
        new_node = Node(value)
        if not head:
            return new_node
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head
    def printList(self, head):
        current = head
        while current:
            print(current.data, end='')
            current = current.next
        print()

class Solution:
    def addOneUtil(self, node):
        if not node:
            return 1
        carry=self.addOneUtil(node.next)
        total = node.data+carry
        node.data = total%10
        return total //10
    def addOne(self,head):
        carry = self.addOneUtil(head)
        if carry:
            new_head = Node(carry)
            new_head.next =head
            head = new_head
        return head

if __name__ == "__main__":
    head = None
    ll = LinkedList()
    sol = Solution()

    # Example: Number 129 (1 -> 2 -> 9)
    head = ll.append(head, 1)
    head = ll.append(head, 2)
    head = ll.append(head, 9)

    print("Original Number: ", end='')
    ll.printList(head)

    head = sol.addOne(head)

    print("After Adding One: ", end='')
    ll.printList(head)
