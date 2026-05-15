from queue import Queue
from collections import deque, defaultdict

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def bottomView(self, root):
        if not root: return []
        mpp = {}
        q = deque([(root, 0)])
        
        while q:
            node, line = q.popleft()
            # ALWAYS update (overwrites with the lower-level node)
            mpp[line] = node.data
                
            if node.left: q.append((node.left, line - 1))
            if node.right: q.append((node.right, line + 1))
                
        return [mpp[k] for k in sorted(mpp)]