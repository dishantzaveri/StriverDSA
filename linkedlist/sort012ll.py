# Node class representing each element of the linked list
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# LinkedList class to manage list operations
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the end
    def insert(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node  
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Function to print the entire linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="")
            if temp.next:
                print(" -> ", end="")
            temp = temp.next
        print(" -> NULL")

class Solution:
    def sortZeroOneTwo(self, ll):
        zero_dummy = Node(-1)
        one_dummy = Node(-1)
        two_dummy = Node(-1)
        zero_tail = zero_dummy
        one_tail = one_dummy
        two_tail = two_dummy

        curr = ll.head
        while curr:
            if curr.data == 0:
                zero_tail.next = curr
                zero_tail = zero_tail.next
            elif curr.data == 1:
                one_tail.next = curr
                one_tail = one_tail.next
            else:
                two_tail.next = curr
                two_tail = two_tail.next
            curr = curr.next
        zero_tail.next = one_dummy.next if one_dummy.next else two_dummy.next
        one_tail.next = two_dummy.next
        two_tail.next = None
        ll.head = zero_dummy.next

# Driver code
if __name__ == "__main__":
    ll = LinkedList()
    sol = Solution()
    ll.insert(1)
    ll.insert(2)
    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(0)

    print("Original List:")
    ll.print_list()
    sol.sortZeroOneTwo(ll)

    print("Sorted List:")
    ll.print_list()
