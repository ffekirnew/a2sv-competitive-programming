from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dictionary = set(wordDict)
        
        @cache
        def dp(curr_index: int) -> List[List[str]]:
            if curr_index == len(s):
                return []
            
            possible_sentences: List[List[str]] = []

            for index in range(curr_index, len(s)):
                curr_word = s[curr_index : index + 1]

                if curr_word in dictionary:
                    following_sentences = dp(index + 1)

                    if following_sentences:
                        possible_sentences += [ [curr_word] + sentence for sentence in following_sentences ]

                    elif index + 1 == len(s):
                        possible_sentences += [ [curr_word] ]
            
            return possible_sentences
        
        return [" ".join(sentence) for sentence in dp(0)]