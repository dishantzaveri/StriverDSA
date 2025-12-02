class Node:
    def __init__(self, val):
        self.num = val
        self.next = None

def insertNode(head, val):
    newNode = Node(val)
    if not head:
        head = newNode
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newNode
    return head
def getDifference(head1, head2):
    len1, len2 = 0, 0
    while head1 or head2:
        if head1:
            len1 += 1
            head1 = head1.next
        if head2:
            len2 += 1
            head2 = head2.next
    return len1 - len2  

def intersectionPresent(head1, head2):
    diff = getDifference(head1, head2)

    if diff < 0:
        diff = -diff
        while diff != 0:
            head2 = head2.next
            diff -= 1
    else:
        while diff != 0:
            head1 = head1.next
            diff -= 1

    while head1:
        if head1 == head2:
            return head1 
        head2 = head2.next
        head1 = head1.next
    return None 

def printList(head):
    while head and head.next:
        print(f"{head.num}->", end="")
        head = head.next
    if head:
        print(head.num, end="")
    print()

head = Node(1)
insertNode(head, 3)
insertNode(head, 1)
insertNode(head, 2)
insertNode(head, 4)
head1 = head
head = head.next.next.next  
headSec = Node(3)
head2 = headSec
headSec.next = head  # Creating intersection

print("List1: ", end="")
printList(head1)
print("List2: ", end="")
printList(head2)

answerNode = intersectionPresent(head1, head2)
if answerNode is None:
    print("No intersection")
else:
    print(f"The intersection point is {answerNode.num}")
