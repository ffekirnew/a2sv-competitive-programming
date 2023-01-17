class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # do selection sort
        for swap_idx in range(len(heights)):
            min_idx = swap_idx

            for idx in range(swap_idx, len(heights)):
                if heights[idx] > heights[min_idx]:
                    min_idx = idx
            
            heights[min_idx], heights[swap_idx] = heights[swap_idx], heights[min_idx]
            names[min_idx], names[swap_idx] = names[swap_idx], names[min_idx]

        return names
        