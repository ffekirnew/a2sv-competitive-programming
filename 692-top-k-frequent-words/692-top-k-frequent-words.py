class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # create the object to be returned
        answer = []
        # count the words
        freq = Counter(words)
        # create a heap and add them words with negative frequencies
        heap = []
        for key, value in freq.items():
            heappush(heap, [-value, key])
        # pop from the heap
        for i in range(k):
            answer.append(heappop(heap)[1])
        # return the solution
        return answer
        