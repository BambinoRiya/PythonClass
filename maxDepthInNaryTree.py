"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        child_depth  = [self.maxDepth(child) for child in root.children]
        
        if child_depth:
            return 1 + max(child_depth)
        else:
            return 1

        


            
        
