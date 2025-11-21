class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def searchValue(self, head, key):
        current = head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

# Driver code
if __name__ == "__main__":
    #  10 -> 20 -> 30
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    obj = Solution()

    if obj.searchValue(head, 206):
        print("Found")
    else:
        print("Not Found")