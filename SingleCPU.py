class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        arr = []

        for i in range(n):
            currTask = tasks[i]
            arr.append((currTask[0],currTask[1],i))

        arr.sort()
        min_heap = []
        answer = []
        index,currTime = 0,0

        while index < n or min_heap:
            if not min_heap and currTime < arr[index][0]:
                currTime = arr[index][0]

            while index < n and currTime >= arr[index][0]:
                heapq.heappush(min_heap, (arr[index][1],arr[index][2]))
                index +=1

            processTime, idx = heapq.heappop(min_heap)
            currTime += processTime
            answer.append(idx)

        return answer

        
