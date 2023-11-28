from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node,visited):
            visited.add(node)
            if node == destination:
                return True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    found = dfs(neighbor,visited)

                    if found:
                        return True
            return False 

        graph = defaultdict(list)
        visited = set()

        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)

        if not edges:
            return True
 

        return dfs(source,visited)

        
      
