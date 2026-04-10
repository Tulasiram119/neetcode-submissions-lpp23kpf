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
        arr = []
        newHead = head
        while newHead:
            arr.append(newHead.val)
            newHead = newHead.next
        left,right = 0,len(arr)-1
        while left <= right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True