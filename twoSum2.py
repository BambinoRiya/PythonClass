class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointsLeft = 0
        pointsRight =len(numbers)-1
        curr_sum = 0

        while numbers[pointsLeft] + numbers[pointsRight] != target:
            curr_sum = numbers[pointsLeft] + numbers[pointsRight]
            if curr_sum < target:
                pointsLeft +=1
            else:
                pointsRight -=1

        return [pointsLeft+1, pointsRight+1]
