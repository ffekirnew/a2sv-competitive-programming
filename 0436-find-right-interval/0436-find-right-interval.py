class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        answer = [None] * len(intervals)
        
        intervals = [ [interval[0], interval[1], i] for i, interval in enumerate(intervals) ]
        intervals.sort()
        
        for i, interval in enumerate(intervals):
            for j in range(i, len(intervals)):
                if intervals[j][0] >= interval[1]:
                    answer[interval[2]] = intervals[j][2]
                    break

            if answer[interval[2]] == None:
                answer[interval[2]] = -1

        return answer