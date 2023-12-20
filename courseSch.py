class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        res = []
        degree_counter = defaultdict(int)
        queue = deque()

        for a,b in prerequisites:
            graph[b].append(a)
            degree_counter[a] +=1

        for course in range(numCourses):
            if degree_counter[course] == 0 or course not in degree_counter:
                queue.append(course)

        while queue:
            course = queue.popleft()
            res.append(course)

            for sub in graph[course]:
                degree_counter[sub] -=1
                if degree_counter[sub] == 0:
                    queue.append(sub)

        if len(res) == numCourses:
            return res
        return []
