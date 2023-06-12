class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return None
        ranges = [[nums[0], nums[0]]]
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                ranges[-1][1] = nums[i]
            else:
                ranges.append([nums[i], nums[i]])
        
        answer = []
        for start, end in ranges:
            if start != end:
                answer.append(f"{start}->{end}")
            else:
                answer.append(str(start))
        
        return answer
        