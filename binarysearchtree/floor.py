class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def floorInBST(self, root, key):
        floor = -1
        while root:
            if root.val == key:
                floor = root.val
                return floor
            if key > root.val:
                floor = root.val
                root = root.right
            else:
                root = root.left
        return floor

def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.val, end=" ")
    printInOrder(root.right)

# Creating a BST
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(13)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(2)
root.left.left.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(14)

print("Binary Search Tree:")
printInOrder(root)
print()

solution = Solution()

# Searching for a value in the BST
target = 8
floorVal = solution.floorInBST(root, target)

if floorVal != -1:
    print(f"Floor of {target} is: {floorVal}")
else:
    print("No floor found!")