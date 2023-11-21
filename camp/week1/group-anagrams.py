class Solution:
    def sortString(self, string: str):
        string = list(string)
        string.sort()
        return "".join(string)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create the object to be returned
        answer = []
        # count the frequencies of the letter in each string
        freqs = {}
        for s in strs:
            s_sorted = self.sortString(s)
            if s_sorted not in freqs:
                freqs[s_sorted] = [s]
            else:
                freqs[s_sorted].append(s)
        for s in freqs.values():
            answer.append(s)
        return answer
        