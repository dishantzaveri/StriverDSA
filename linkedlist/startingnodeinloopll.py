class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)

    # Create cycle (last node points to node with value 2)
    head.next.next.next.next = head.next

    obj = Solution()
    result = obj.detectCycle(head)

    if result:
        print("Cycle starts at node with value:", result.val)
    else:
        print("No cycle found.")
