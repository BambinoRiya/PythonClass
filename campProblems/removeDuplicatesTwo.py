# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import Counter
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = ListNode(None, head)
        current = head
        ans = previous

        while current and current.next:
            if current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                previous.next = current.next
            else:
                previous = previous.next
            current = current.next
        return ans.next

#Time complexity : O(n)
#Space complexity : O(n)
