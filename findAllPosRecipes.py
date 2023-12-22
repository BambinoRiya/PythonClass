class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        in_deg = defaultdict(int) #for in-degree
        res = []
        graph = defaultdict(list)
        queue = deque()

        for r in recipes:
            in_deg[r] = 0
        for s in supplies:
            in_deg[s] = 0
        print(in_deg)

        #now do the in-degree
        for r in range(len(recipes)):
            for i in ingredients[r]:
                graph[i].append(recipes[r])
                in_deg[recipes[r]] +=1
        print(graph)

        for val in in_deg:
            if in_deg[val] == 0:
                queue.append(val)

        while queue:
            curr = queue.popleft()

            if curr not in supplies:
                res.append(curr)

            for neighbor in graph[curr]:
                in_deg[neighbor] -=1

                if in_deg[neighbor] == 0:
                    queue.append(neighbor)


        return res

        
