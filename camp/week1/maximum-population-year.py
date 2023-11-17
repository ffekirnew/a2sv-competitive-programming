class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # preprocess
        population = []
        for birth_year, death_year in logs:
            population.append([birth_year, 1])
            population.append([death_year, 0])
        
        population.sort()
        
        # formulate answer
        max_population, max_population_year = -inf, None
        curr_population = 0
        for log in population:
            year, log_type = log
            
            if log_type == 1:
                curr_population += 1
            else:
                curr_population -= 1
            
            if curr_population > max_population:
                max_population = curr_population
                max_population_year = year
        
        return max_population_year
                