from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = (int(lock[i]) + 1) % 10
                res.append(lock[:i] + str(digit) + lock[i+1:])
                digit = (int(lock[i]) - 1 + 10) % 10
                res.append(lock[:i] + str(digit) + lock[i+1:])
            return res

        queue = deque()
        queue.append(('0000', 0))
        visited = set(deadends)

        while queue:
            lock, count = queue.popleft()
            if lock == target:
                return count

            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    queue.append((child, count + 1))

        return -1
