class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        queue = deque([rooms[0]])  

        while queue:
            keys = queue.popleft()

            for key in keys:
                if key not in visited:
                    visited.add(key)
                    queue.append(rooms[key])   

        if len(visited) == len(rooms):
            return True
        else:
            return False   
