class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n < 2:
            return n
        else:
            lst = [i for i in range(1, n + 1)]
            i = 0
            while len(lst) > 1:
                i = (i + k - 1) % len(lst)
                lst.pop(i)
            return int(lst[0])