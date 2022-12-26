class Solution:
    def set_counter(self, string: str):
        return set([c for c in string])
    def similarPairs(self, words: List[str]) -> int:
        answer = 0
        set_of_words = [self.set_counter(word) for word in words]
        for i in range(len(set_of_words)):
            for j in range(i + 1, len(set_of_words)):
                if set_of_words[i] == set_of_words[j]:
                    answer += 1
        return answer
        