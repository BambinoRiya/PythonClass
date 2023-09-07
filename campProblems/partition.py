# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        current = head
        left , right= ListNode(0), ListNode(0)
        leftTail , rightTail = left, right

        while current:
            if current.val < x:
                leftTail.next = current
                leftTail = leftTail.next
            else:
                rightTail.next = current
                rightTail = rightTail.next
            
            current = current.next

        leftTail.next = None
        rightTail.next = None

        leftTail.next = right.next
        
        return left.next
        
