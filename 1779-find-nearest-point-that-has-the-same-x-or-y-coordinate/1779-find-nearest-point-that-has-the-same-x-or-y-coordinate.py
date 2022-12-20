class Solution:
    def manhattan_distance(self, x: int, y: int, point: List[int]):
        return abs(x - point[0]) + abs(y - point[1])
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        man_dis = float('inf')
        answer = -1
        for i, point in enumerate(points):
            if x == point[0] or y == point[1]:
                if man_dis > self.manhattan_distance(x, y, point):
                    man_dis = self.manhattan_distance(x, y, point)
                    answer = i
        return answer
        