class UnionFind:
    def __init__(self,words):   
        self.root = {word:word for word in words}
    
    def find(self, node):
        if node == self.root[node]:
            return node
        return self.find(self.root[node])

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if root_x < root_y:
                self.root[root_y] = root_x
            else:
                self.root[root_x] = root_y


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        words = set(s1 + s2 + baseStr)
        graph = UnionFind(words)
        res = ""

        for i in range(len(s1)):
            graph.union(s1[i],s2[i])

        for char in baseStr:
            res += graph.find(char)

        return res


              
