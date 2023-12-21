from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        counter = defaultdict(int)
        queue = deque()
        N = len(graph)
        res = []

        # :( @ 9:25 PM
        for i in range(N):
            for node in graph[i]:
                adj_list[node].append(i)
                counter[i] +=1
    
        #find terminal
        for node in range(N):
            if node not in counter:
                queue.append(node)
        # print(adj_list)
        # print(counter)

        #bfs logiccccc
        while queue:
            node = queue.popleft()
            res.append(node)
            #find neighbors of newly popped node nad append then reduce count

            for neighbor in adj_list[node]:
                counter[neighbor] -=1
                if counter[neighbor] == 0:
                    queue.append(neighbor)

        res.sort()
        return res

        
