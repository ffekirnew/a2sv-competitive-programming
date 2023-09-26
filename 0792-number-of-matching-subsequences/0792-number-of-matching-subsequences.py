class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = [None for __ in range(len(s) + 1)]
        for i in range(len(s) - 1, -2, -1):
            if i == len(s) - 1:
                trie[i + 1] = {}
            else:
                new_trie_node = trie[i + 2].copy()
                new_trie_node[s[i + 1]] = i + 1

                trie[i + 1] = new_trie_node

        counter = 0
        for word in words:
            trie_index = 0
            is_subsequence = True

            for i, char in enumerate(word):
                if char not in trie[trie_index]:
                    is_subsequence = False
                    break
                
                trie_index = trie[trie_index][char] + 1
            
            if is_subsequence:
                counter += 1
        
        return counter
                
                
                    
                
                
            
                
