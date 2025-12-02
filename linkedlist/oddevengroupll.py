
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        odd = head                 
        even = head.next            
        even_head = even            

        while even and even.next:
            odd.next = even.next     
            odd = odd.next

            even.next = odd.next     
            even = even.next

        odd.next = even_head

        return head

def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    temp = head
    for val in arr[1:]:
        temp.next = ListNode(val)
        temp = temp.next
    return head

def print_list(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    head1 = build_list(arr1)
    print("Original List 1:", end=" ")
    print_list(head1)

    sol = Solution()
    result1 = sol.oddEvenList(head1)

    print("Odd-Even List 1:", end=" ")
    print_list(result1)

    arr2 = [2, 1, 3, 5, 6, 4, 7]
    head2 = build_list(arr2)
    print("Original List 2:", end=" ")
    print_list(head2)

    result2 = sol.oddEvenList(head2)

    print("Odd-Even List 2:", end=" ")
    print_list(result2)
