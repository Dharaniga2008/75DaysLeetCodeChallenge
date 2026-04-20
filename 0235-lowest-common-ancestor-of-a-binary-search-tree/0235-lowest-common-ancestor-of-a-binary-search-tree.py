# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            # If both nodes are smaller, go left
            if p.val < root.val and q.val < root.val:
                root = root.left
            
            # If both nodes are greater, go right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            # This is the split point → LCA
            else:
                return root