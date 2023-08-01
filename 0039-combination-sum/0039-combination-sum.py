class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = {candidate: set([(candidate,)]) for candidate in candidates}
        
        for number in range(2, target + 1):
            for candidate in candidates:
                if number - candidate in combinations:
                    if number not in combinations:
                        combinations[number] = set()

                    for partial_combination_1 in combinations[candidate]:
                        for partial_combination_2 in combinations[number - candidate]:
                            combination = partial_combination_1 + partial_combination_2
                            combinations[number].add(tuple(sorted(combination)))
        
        return combinations[target] if target in combinations else []
                        
            
            
        