class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


class Solution:
    def insertAtHead(self,head,newData):
        newNode = Node(newData, head)
        return newNode
    
    def printList(self,head):
        temp=head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()
        
if __name__ == "__main__":
    sol = Solution()

    #  sample linked list: 2 -> 3
    head = Node(2)
    head.next = Node(3)

    print("Original List:", end=" ")
    sol.printList(head)

    # Inserting new node at head
    head = sol.insertAtHead(head, 1)

    print("After Insertion at Head:", end=" ")
    sol.printList(head)