# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        string = ""
        curr = head
        while curr:
            string += str(curr.val)
            curr = curr.next
        new_string = string[::-1]
        print(string, new_string)
        if string == new_string:
            return True
        return False
