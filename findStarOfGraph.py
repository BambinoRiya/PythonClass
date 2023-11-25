from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)

        res = []

        for i in graph:
            if len(graph[i]) > 1:
                res = i
                break
        return res
        
