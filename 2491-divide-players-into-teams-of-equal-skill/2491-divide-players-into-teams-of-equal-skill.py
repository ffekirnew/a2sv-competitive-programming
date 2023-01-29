class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sum_chemistry = 0
        
        # sort the skills
        skill.sort()
        
        # set up two pointers
        teams = []
        
        left = 0
        right = len(skill) - 1
        
        
        # form the teams
        while left < right:
            teams.append(tuple([skill[left], skill[right]]))
            left += 1
            right -= 1
            
        # check if all teams have the same skills
        sum_skill = sum(teams[0])
        
        for team in teams:
            if sum(team) != sum_skill:
                return -1
            sum_chemistry += team[0] * team[1]
        
        return sum_chemistry
            
        