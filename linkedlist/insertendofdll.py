class Node:
    def __init__(self, data, next_node=None, back_node=None):

        self.data = data
        self.next = next_node
        self.back = back_node

def convertArr2DLL(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp
    return head

def print_list(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

def insert_at_tail(head, k):
    new_node = Node(k)
    if head is None:
        return new_node
    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = new_node
    new_node.back = tail

    return head

# Main program
arr = [12, 5, 8, 7, 4]
head = convertArr2DLL(arr)
print("\nDoubly Linked List Initially:")
print_list(head)
print("\nDoubly Linked List After Inserting at the tail with value 10:")
# Insert a node with value 10 at the end
head = insert_at_tail(head, 10)
print_list(head)