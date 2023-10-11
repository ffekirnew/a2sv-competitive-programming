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
                if self.rating[index] < self.rating[other_number_index]:
                    decreasing_ending_at[index] += 1
                    teams_count += decreasing_ending_at[other_number_index]
                    
        return teams_count


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        solution = CountNumberOfTeams(rating)
        return solution.bottom_up()
        