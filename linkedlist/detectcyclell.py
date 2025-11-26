class Node:

    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

class Solution:
    def detectLoop(self, head):
        temp=head
        nodeMap={}
        while temp is not None:
            if temp in nodeMap:
                return True
            nodeMap[temp] = 1
            temp=temp.next
        return False
        
        
if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # fifth.next = third

    sol = Solution()
    if sol.detectLoop(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")