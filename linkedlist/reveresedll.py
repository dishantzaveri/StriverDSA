class Node:
    def __init__(self, data, next_node=None, back_node=None):
        self.data = data
        self.next = next_node
        self.back = back_node

def convert_arr_to_dll(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp
    return head

def print_dll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

def reverse_dll(head):
    if head is None or head.next is None:
        return head
    prev = None  
    current = head  

    while current is not None:

        prev = current.back 
        current.back = current.next
        current.next = prev 
        current = current.back  
    return prev.back

# Example usage:
arr = [12, 5, 6, 8, 4]
head = convert_arr_to_dll(arr)
# Print the doubly linked list
print('Doubly Linked List Initially:  ')
print_dll(head)

print('Doubly Linked List After Reversing :')

head = reverse_dll(head)
print_dll(head)
