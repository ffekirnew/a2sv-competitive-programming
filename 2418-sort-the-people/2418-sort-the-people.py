class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # do selection sort
        for idx in range(1, len(heights)):
            curr_idx = idx
            
            while curr_idx > 0:
                if heights[curr_idx] > heights[curr_idx - 1]:
                    heights[curr_idx], heights[curr_idx - 1] = heights[curr_idx - 1], heights[curr_idx]
                    names[curr_idx], names[curr_idx - 1] = names[curr_idx - 1], names[curr_idx]
                    curr_idx -= 1
                else:
                    break
        return names
        