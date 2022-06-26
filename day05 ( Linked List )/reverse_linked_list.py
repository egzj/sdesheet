# Date Completed: 26th June 2022
# Resources:
# 1. https://www.youtube.com/watch?v=iRtLEoL-r-g&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=28


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oldNode = None

        # loop
        while head is not None:
            nextNode = head.next  # 2,3,4,5,None
            head.next = oldNode  # None,1,2,3,4
            oldNode = head  # 1,2,3,4,5
            head = nextNode  # 2,3,4,5,None

        return oldNode


# Time Complexity: O(n)
# Space Complexity: O(1)

# Success
# Details
# Runtime: 51 ms, faster than 57.61% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.4 MB, less than 55.36% of Python3 online submissions for Reverse Linked List.
