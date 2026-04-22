# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):
        
        def validate(node, low, high):
            if not node:
                return True
            
            # Check current node value
            if node.val <= low or node.val >= high:
                return False
            
            # Check left and right subtree
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root, float('-inf'), float('inf'))