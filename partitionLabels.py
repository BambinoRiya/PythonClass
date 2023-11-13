class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index_check= {}

        for i, c in enumerate(s):
            index_check[c] = i
        
        res = []
        end,size = 0,0
        for i, c in enumerate(s):
            size +=1
            end = max(end, index_check[c])
        
            if i == end:
                res.append(size)
                size =0

        return res

        #time complexity : O(n)
        #space complexity: O(1)
