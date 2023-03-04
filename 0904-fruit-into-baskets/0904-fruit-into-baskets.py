class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        f1, f2 = None, None # going to hold values [ type_of_fruit, last_seen_index, first_seen_index ]
        maximum = 0
        
        l, r = 0, 0
        freq = defaultdict(int)
        
        l = 0
        for r, curr_fruit in enumerate(fruits):
            freq[curr_fruit] += 1
            
            while len(freq) > 2:
                freq[fruits[l]] -= 1
                
                if not freq[fruits[l]]:
                    del freq[fruits[l]]
                
                l += 1
            
            maximum = max( maximum, r - l + 1 )
        
        return maximum
        