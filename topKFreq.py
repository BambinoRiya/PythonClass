from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        res = []
        heap = [(-values, key) for key, values in count.items()]
        heapify(heap)
        
        while len(res) < k:
            res.append(heappop(heap)[1])
        return res

        #time : O(n)
        #space : O(n)
        
