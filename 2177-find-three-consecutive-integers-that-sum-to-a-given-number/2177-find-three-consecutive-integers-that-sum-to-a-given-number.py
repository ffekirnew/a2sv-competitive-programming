class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # check if number can be devided by 3
        if num % 3 == 0:
            return [num // 3 - 1, num // 3, num // 3 + 1]

        return []