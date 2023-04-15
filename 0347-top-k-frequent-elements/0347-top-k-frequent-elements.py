class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create the object to be returned
        answer = []
        # count the elements
        freqs = Counter(nums)
        # create a heap and add all counts and elements in there
        heap = []
        for freq in freqs.keys():
            heappush(heap, [-1 * freqs[freq], freq])
        # pop untill k
        for i in range(k):
            answer.append(heappop(heap)[1])
        # return answer
        return answer
        