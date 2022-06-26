# # Date Completed: 26th June 2022
# Problem Link: https://www.codingninjas.com/codestudio/problems/2099908
# *Copied the model answer, as it was better than my simple solution

"""
    Time Complexity : O(q)
    Space Complexity : O(q)

    Where q is the number of queries.
"""


class Queue:
    def __init__(self):

        # Intialise the queue with 0 elements.
        self.rear = 0
        self.qfront = 0
        self.size = 0
        self.queueSize = 100010
        self.q = [0 for i in range(100010)]

    # Function to check if the queue is empty.
    def isEmpty(self):

        if self.qfront == self.rear:
            return True

        return False

    def enqueue(self, data):

        # Push the current element in the queue.
        self.q[self.rear] = data
        self.rear = self.rear + 1

        # Increase the value of size.
        self.size += 1

    def dequeue(self):

        # Check if the queue is empty.
        if self.isEmpty():
            return -1

        ans = self.q[self.qfront]
        self.qfront += 1
        self.size -= 1

        if self.qfront == self.rear:
            self.qfront = 0
            self.rear = 0

        return ans

    def front(self):

        # Check if the queue is empty.
        if self.isEmpty():
            return -1

        # Return the element at front.
        return self.q[self.qfront]
