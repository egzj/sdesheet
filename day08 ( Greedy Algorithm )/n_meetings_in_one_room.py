# Date Completed: 26th June 2022
# Problem Link: https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
# References:
# 1. https://www.youtube.com/watch?v=II6ziNnub1Q&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=46

# Function to find the maximum number of meetings that can
# be performed in a meeting room.
def maximumMeetings(self, n, start, end):

    # Space Complexity: O(n)
    # Time Complexity: O(n)
    meetings = [(start[i], end[i], i + 1) for i in range(len(start))]  # meeting is 1-indexed

    # sort meetings according to end time DESC and index ASC
    # Space Complexity: O(1) - because sorting is in place
    # Time Complexity: O(nlogn)
    meetings.sort(key=lambda tup: (tup[1], tup[2]))  # time complexity

    count = 0
    current_max = -1  # used to track the current maximum end time

    # loop through meetings
    for (s, e, meeting_num) in meetings:
        if s > current_max:
            count += 1
            current_max = e

    return count


# Time Complexity: O(n) + O(nlogn) +O(n)
# Space Complexity: O(1)
