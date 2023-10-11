"""
Solution Steps:
1. Iterate over each rating
    1.1. For every rating, iterate over other ratings before it, since we want subsequences
        1.1.1. If original rating is greater, update ending at that index and count the teams that can be formed based on the other index
        1.1.2. If less, do the same but for decreasing ending at that index and count it
2. Return the count

Complexity Analysis:
- Time Complexity: O(n ^ 2)
- Space Complexity: O(n)
    where: n is the length of the ratings list
"""


class CountNumberOfTeams:
    def __init__(self, rating: List[int]):
        self.rating = rating

    def bottom_up(self) -> int:
        teams_count = 0

        increasing_ending_at = [0 for index in range(len(self.rating))]
        decreasing_ending_at = [0 for index in range(len(self.rating))]

        for index in range(len(self.rating)):
            for other_number_index in range(0, index):
                if self.rating[index] > self.rating[other_number_index]:
                    increasing_ending_at[index] += 1
                    teams_count += increasing_ending_at[other_number_index]
                elif self.rating[index] < self.rating[other_number_index]:
                    decreasing_ending_at[index] += 1
                    teams_count += decreasing_ending_at[other_number_index]
                    
        return teams_count


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        solution = CountNumberOfTeams(rating)
        return solution.bottom_up()
        