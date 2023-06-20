from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = []
        losers = []
        for x in range(len(matches)):
            winners.append(matches[x][0])
            losers.append(matches[x][1])

        count_winners = Counter(winners)
        count_losers = Counter(losers)

        res1 = list(set(count_winners.keys()) - set(count_losers.keys()))
        res2 = [num for num, value in count_losers.items() if value == 1]

        return [sorted(res1), sorted(res2)]

        """
         time complexity: O(N)
         space complexity: O(N)
        """
    
