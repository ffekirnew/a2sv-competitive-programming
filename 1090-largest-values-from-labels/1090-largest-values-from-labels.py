class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        # create the obj. to be returned
        result = 0
        
        # zip the values and labels together and sort it
        pairs = [[labels[i], values[i]] for i in range(len(values))]
        pairs.sort(key = lambda x: x[1], reverse = True)
        
        # create a dictionary to keep track of what's been added
        used = defaultdict(int)
        count = 0
        for pair in pairs:
            if count == numWanted:
                break
            
            if used[pair[0]] < useLimit:
                result += pair[1]
                used[pair[0]] += 1
                count += 1

        # return the solution
        return result
        
        