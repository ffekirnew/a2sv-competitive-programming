class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # loop from n and onwards
        iterator = n
        while (True):
            if iterator % 2 == iterator % n:
                return iterator
            iterator += 1