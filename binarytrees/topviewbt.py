
from collections import deque 
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    def topView(self, root):
        if not root: return []
        mpp = {} # Dictionary to store {line: node_data}
        q = deque([(root, 0)])
        
        while q:
            node, line = q.popleft()
            # ONLY update if the line is not in the map
            if line not in mpp:
                mpp[line] = node.data
                
            if node.left: q.append((node.left, line - 1))
            if node.right: q.append((node.right, line + 1))
                
        return [mpp[k] for k in sorted(mpp)]
    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(10)
    root.left.left.right = Node(5)
    root.left.left.right.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(10)
    root.right.left = Node(9)

    # Create Solution object
    solution = Solution()

    # Get the top view
    result = solution.topView(root)

    # Print the result
    print("Top View Traversal:", *result)