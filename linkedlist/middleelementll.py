class Node:
    def __init__(self, data, next_node=None):
        self.data = data       
        self.next = next_node  
        
def find_mid(head):
    slow=head
    fast=head
    while fast and fast.next and slow:
        fast=fast.next.next
        slow=slow.next
    return slow
        
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(3)

middle_node = find_mid(head)

print("The middle node value is:", middle_node.data)