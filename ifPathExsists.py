class UnionFind:
    def __init__(self,n):
        self.root = {n:n for n in range(n)}
        self.size = {n:1 for n in range(n)}

    def find(self,node):
        if node ==  self.root[node]:
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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = UnionFind(n)

        for i,j in edges:
                graph.union(i,j)

        return graph.find(source) == graph.find(destination)
