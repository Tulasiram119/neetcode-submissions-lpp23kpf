# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # We have list and we need to find weather it is a paindrome or not
        # How can we do that ?
        # If it is an array we can have both start and end and check for equality
        # but it is a linked list we can only move in one direction.
        # One more thing we can reverse the linked the list and compare them
        # or We can find the mid point and reverse from the that point.
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        left,right = head,prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
