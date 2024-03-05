class UnionFind:
    def __init__(self,n):
        self.root = {n:n for n in range(n)}
        self.size = {n:1 for n in range(n)}

    def find(self,node):
        if node == self.root[node]:      
            return node
        else:
            return self.find(self.root[node])

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.size[root_x] > self.size[root_y]:
                self.root[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            else:
                self.root[root_x] = root_y
                self.size[root_y] += self.size[root_x]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        count = 0
        graph = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph.union(i,j)

        for val in graph.root:
            if graph.root[val] == val:
                count +=1
        print(graph)
        return count

