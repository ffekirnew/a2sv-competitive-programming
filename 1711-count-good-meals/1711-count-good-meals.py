class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        # create the power to be returned
        answer = 0
        # convert deliciousness into a dictionary for an O(1) key lookup
        seen = {deliciousness[0]: 1}
        for i in range(1, len(deliciousness)):
            food = deliciousness[i]
            for i in range(22):
                power = 2 ** i
                answer += seen.get(power - food, 0)
            seen[food] = seen.get(food, 0) + 1
        # return the solution
        return answer%(10 ** 9 + 7)
            
        