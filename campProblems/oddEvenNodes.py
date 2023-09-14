# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode(None)
        even = ListNode(None)
        odd_head = odd
        even_head = even
        current = head
        count = 1

        while current:
            if count % 2 > 0:
                odd.next = current
                odd = odd.next
            else:
                even.next = current
                even = even.next
            current = current.next
            count += 1
        odd.next = even_head.next
        even.next = None 
        return odd_head.next

        
