class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        answer = []
        
        for spell in spells:
            answer.append( len(potions) - bisect_left( potions, ceil(success / spell) ) )
        
        return answer
        