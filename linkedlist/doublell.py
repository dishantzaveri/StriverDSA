
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

arr = [2, 5, 8, 7]
head = Node(arr[0])
print(head)
print(head.data)
