class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        a_count = 0
        b_count = 0
        n = len(costs)/2
        
        costs.sort(key= lambda x: abs(x[1]-x[0]), reverse = True)

        i = 0
        for cost in costs:
            minn = min(cost)
            if a_count < n and b_count < n:
                if costs[i].index(minn) == 0:
                    res+=minn
                    a_count+=1
                else:
                    b_count+=1
                    res+=cost[1]
            elif a_count == n:
                b_count +=1
                res+=cost[1]
            else:
                a_count+=1
                res+=cost[0]
            i+=1
        
        

        return res
