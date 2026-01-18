

# Node structure
class Node:
    def __init__(self, d):
        self.val = d
        self.next = None

# Structure to represent stack
class LinkedListStack:
    def __init__(self):
        self.head = None  # Top of Stack
        self.size = 0  # Size

    # Method to push an element onto the stack
    def push(self, x):
        # Creating a node
        element = Node(x)
        
        element.next = self.head  # Updating the pointers
        self.head = element  # Updating the top
        
        # Increment size by 1
        self.size += 1

    # Method to pop an element from the stack
    def pop(self):
        # If the stack is empty
        if self.head is None:
            return -1  # Pop operation cannot be performed
        
        value = self.head.val  # Get the top value
        temp = self.head  # Store the top temporarily
        self.head = self.head.next  # Update top to next node
        del temp  # Delete old top node
        self.size -= 1  # Decrement size
        
        return value  # Return data

    # Method to get the top element of the stack
    def top(self):
        # If the stack is empty
        if self.head is None:
            return -1  # Top element cannot be accessed
        
        return self.head.val  # Return the top

    # Method to check if the stack is empty
    def isEmpty(self):
        return self.size == 0

# Creating a stack
st = LinkedListStack()

# List of commands
commands = ["LinkedListStack", "push", "push", "pop", "top", "isEmpty"]
# List of inputs
inputs = [[], [3], [7], [], [], []]

for i in range(len(commands)):
    if commands[i] == "push":
        st.push(inputs[i][0])
        print("null", end=" ")
    elif commands[i] == "pop":
        print(st.pop(), end=" ")
    elif commands[i] == "top":
        print(st.top(), end=" ")
    elif commands[i] == "isEmpty":
        print("true" if () else "false", end=" ")
    elif commands[i] == "LinkedListStack":
        print("null", end=" ")