class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary = salary[1:-1]
        average = sum(salary) / len(salary)
        return average
