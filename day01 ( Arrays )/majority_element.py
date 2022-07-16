# Date Completed: 16th July 2022
# Problem Link: https://leetcode.com/problems/majority-element/
# References:
# 1. https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        votes = 0

        # Finding majority candidate
        for i in range(len(nums)):
            if votes == 0:
                candidate = nums[i]
                votes = 1
            else:
                if nums[i] == candidate:
                    votes += 1
                else:
                    votes -= 1
        return candidate
