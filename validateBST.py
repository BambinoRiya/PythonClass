# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def checker(node,lower,upper):
            if not node:
                return True
            if not(lower < node.val < upper):
                return False
            return checker(node.right,node.val,upper) and checker(node.left,lower,node.val)
        
        lower = float("-inf")
        upper = float("inf")

        return checker(root,lower,upper)        
