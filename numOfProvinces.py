class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n  
        provinces = 0  

        def dfs(city):
            visited[city] = 1  
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)  


        for city in range(n):
            if not visited[city]:
                provinces += 1 
                dfs(city)  

        return provinces
