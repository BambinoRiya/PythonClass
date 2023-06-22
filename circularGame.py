lass Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friendList = [i for i in range(1,n+1)]
        counter = 0

        while len(friendList) > 1:
            counter = (counter + k -1 ) % len(friendList)
            friendList.pop(counter)

        return friendList[0]

      #Time complexity O(nk), space complexity is O(n)
