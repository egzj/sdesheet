# Date Completed: 26th June 2022
# References:
# 1. https://www.youtube.com/watch?v=sGdwSH8RK-o

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_1 = head
        dummy_2 = head
        while dummy_2 and dummy_2.next:
            dummy_1 = dummy_1.next
            dummy_2 = dummy_2.next.next
        return dummy_1


# Time Complexity: O(n/2)
# Space Complexity: O(1)

# Success
# Details
# Runtime: 33 ms, faster than 88.97% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.8 MB, less than 54.49% of Python3 online submissions for Middle of the Linked List.

#########################################
#            SLOWER METHOD
#########################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # get size of linkedlist
#         size = 1
#         tempHead = head
#         while tempHead.next:  # O(n)
#             size += 1
#             tempHead = tempHead.next

#         # get middle node index
#         middleNodeIndex = int(size / 2)
#         print("middleNodeIndex", middleNodeIndex)

#         # traverse and get middle node
#         index = 0
#         middleNode = head
#         while middleNode.next:  # O(n/2)
#             index += 1
#             middleNode = middleNode.next
#             if index == middleNodeIndex:
#                 break

#         return middleNode


# Time Complexity: O(n) + O(n/2)
# Space Complexity: O(1)

# Success
# Details
# Runtime: 74 ms, faster than 5.53% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.9 MB, less than 10.63% of Python3 online submissions for Middle of the Linked List.
