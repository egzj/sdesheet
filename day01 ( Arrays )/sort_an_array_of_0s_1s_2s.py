# Date Completed: 29th June 2022
# Problem Link: https://leetcode.com/problems/sort-colors/
# References:
# 1. https://www.techiedelight.com/sort-array-containing-0s-1s-2s-dutch-national-flag-problem/
# 2. https://www.youtube.com/watch?v=oaVa-9wmpns&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=4

# References 

# Dutch national flag problem

class Solution:
    
    # Utility function to swap elements `A[i]` and `A[j]` in the list
    def swap(self, A, i, j):

        temp = A[i]
        A[i] = A[j]
        A[j] = temp

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = mid = 0
        pivot = 1
        end = len(nums) - 1

        while mid <= end:
            if nums[mid] < pivot:      # current element is 0
                self.swap(nums, start, mid)
                start = start + 1
                mid = mid + 1
            elif nums[mid] > pivot:    # current element is 2
                self.swap(nums, mid, end)
                end = end - 1
            else:                   # current element is 1
                mid = mid + 1
