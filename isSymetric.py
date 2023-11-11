# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftt = root.left
        rightt = root.right

        if not root:
            return None
        
        def checker(left_node,right_node):
            if not left_node and not right_node:
                return True
            if (not left_node or not right_node) or not(left_node.val == right_node.val):
                return False

            check1 = checker(left_node.left,right_node.right)
            check2 = checker(left_node.right,right_node.left)

            return check1 and check2

        return checker(leftt,rightt)
        
