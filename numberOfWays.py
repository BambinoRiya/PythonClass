from collections import defaultdict
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        def dijkstra(src,dest):
            min_heap = [(0,src)]
            heapq.heapify(min_heap)
            all_paths = {}
    
            while min_heap:
                weight1,node1 = heapq.heappop(min_heap)     
                if node1 in all_paths:continue
                all_paths[node1] = weight1 

                for weight2, node2 in graph[node1]: #checking the children
                    if node2 not in all_paths:
                        heapq.heappush(min_heap,(weight1+weight2,node2))
                        
            return all_paths

        graph = defaultdict(list)

        for src,dest,time in roads:
            graph[src].append((time,dest))
            graph[dest].append((time,src))
        
        all_paths = dijkstra(0,n-1)
        # all_paths = [val for val in all_paths.values()] 
        # print(all_paths)
        
        @cache
        def dp(node, summ):
            if node == 0:
                return 1
            
            count = 0
            for time,neigh in graph[node]:
                if time + summ + all_paths[neigh] == all_paths[n-1]:
                    count += dp(neigh, summ+time)
            
            return count

        return dp(n-1,0) %(10**9 + 7)

      

                
        
