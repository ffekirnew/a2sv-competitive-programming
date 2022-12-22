class Solution:
    def set_counter(self, string: str):
        return set([c for c in string])
    def similarPairs(self, words: List[str]) -> int:
        answer = 0
        for i in range(len(words)):
            word1_dict = self.set_counter(words[i])
            for j in range(i + 1, len(words)):
                word2_dict = self.set_counter(words[j])
                if word1_dict == word2_dict:
                    answer += 1
        return answer
        