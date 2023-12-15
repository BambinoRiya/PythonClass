# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        queue = deque()
        queue.append((root,0))

        while queue:
            curr, adder = queue.popleft()

            if not curr:
                continue
            if not curr.right and not curr.left:
                total =  adder + curr.val
                if total == targetSum:
                    return True
                continue
            
            queue.append((curr.left,adder + curr.val))
            queue.append((curr.right,adder + curr.val))

        return False
            


    
