#Dijkstra's Algorithm version

import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src, dest, time in times:
            adj[src].append((time,dest))
        
        all_paths = defaultdict(list)
        min_heap = [(0,k)]
        heapq.heapify(min_heap)
        ans = []
        while min_heap:   
            w1,n1 = heapq.heappop(min_heap)
            if n1 in all_paths:continue
            all_paths[n1] = w1
            ans.append(w1)
            

            for w2,n2 in adj[n1]:
                if n2 not in all_paths:
                    heapq.heappush(min_heap,(w1+w2,n2))
 
        if len(all_paths) == n:
            return ans[-1]
        else:
            return -1
