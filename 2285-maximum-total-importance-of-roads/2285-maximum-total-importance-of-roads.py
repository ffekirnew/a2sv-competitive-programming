class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # change roads to be a one directional array
        roads_1d = []
        for road in roads:
            a, b = road
            roads_1d.append(a)
            roads_1d.append(b)
        
        freq = list(Counter(roads_1d).values())
        freq.sort(reverse = True)
        
        answer = 0
        
        for val in freq:
            answer += n * val
            n -= 1
        
        return answer
            