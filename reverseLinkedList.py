# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None # A
        current = head # B
        while current:
            next_node = current.next 
            current.next = previous # B.next = a 
            previous = current # A = B 
            current = next_node # B = C 

        return previous
        
        
