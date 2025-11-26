
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

class Solution:
    def lengthOfLoop(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return self.countLoopLength(slow)
        return 0

    def countLoopLength(self, meetingPoint):
        temp = meetingPoint
        length = 1
        while temp.next != meetingPoint:
            temp = temp.next
            length += 1
        return length


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
    # fifth.next = second

    obj = Solution()
    loopLength = obj.lengthOfLoop(head)
    if loopLength > 0:
        print("Length of the loop:", loopLength)
    else:
        print("No loop found in the linked list.")
