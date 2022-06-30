# Date Completed: 30th June 2022
# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/
# References:
# 1. https://www.youtube.com/watch?v=Xb4slcp1U38&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=30
# 2. https://leetcode.com/problems/merge-two-sorted-lists/discuss/789623/merge-two-sorted-lists-with-explanation-in-python
# * Couldn't get the answer, learnt from the model answer instead.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #creating a node for showing result 
        resultList = ListNode()
        ref = resultList
        
        #if both input list is emtpy then return empty list 
        if list1 is None and list2 is None:
            return resultList.next
        #if one list is empty then return another list     
        if list1 is None:
            return list2
        #if one list is empty then return another list     
        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
            resultList = list1
            list1 = list1.next
        else:
            resultList = list2
            list2 = list2.next
        ref = resultList
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                ref.next = list1
                ref = ref.next
                list1 = list1.next
            else:
                ref.next = list2
                ref = ref.next
                list2 = list2.next
        if list1 is None:
            ref.next = list2
        else:
            ref.next = list1
            
        return resultList