# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []
        queue = deque()

        if root:
            queue.append(root)

        while queue:
            curr_level_count = len(queue)
            total = 0

            for i in range(curr_level_count):
                curr = queue.popleft()
                total += curr.val

                # curr_average = total/len(qu)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            averages.append(total/curr_level_count)

        return averages


        
