"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hashmap = {employee.id:employee for employee in employees}
        print(hashmap)

        def dfs(e_id):
            employee = hashmap[e_id]

            total = employee.importance

            if employee.subordinates:
                for sub in employee.subordinates:
                    total += dfs(sub)
            return total

        return dfs(id)


        
        
            

           
                
