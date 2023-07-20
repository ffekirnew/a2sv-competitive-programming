import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        height_diffs = []
        heights_jumped = 0

        for i in range(1, len(heights)):
            height_diff = heights[i - 1] - heights[i]

            if height_diff < 0:
                heapq.heappush(height_diffs, height_diff)
                heights_jumped -= height_diff

            if heights_jumped > bricks:
                if not ladders:
                    return i - 1
                ladders -= 1
                popped = heapq.heappop(height_diffs)
                heights_jumped += popped

        return len(heights) - 1
        