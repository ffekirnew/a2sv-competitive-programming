class Solution:
    def distance(self, pt1, pt2):
        return ((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2) ** 0.5
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = [0] * len(queries)
        
        for i, query in enumerate(queries):
            *center, radius = query

            for pt in points:
                if self.distance(center, pt) <= radius:
                    answer[i] += 1
        
        return answer
                
            
        