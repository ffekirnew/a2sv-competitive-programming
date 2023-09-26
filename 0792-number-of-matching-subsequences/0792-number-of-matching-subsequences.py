class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = [None for _ in range(len(s) + 1)]

        for index in range(len(s) - 1, -2, -1):
            if index == len(s) - 1:
                trie[index + 1] = {}
            else:
                new_trie_node = trie[index + 2].copy()
                new_trie_node[s[index + 1]] = index + 1

                trie[index + 1] = new_trie_node

        subsequence_counter = 0
        for word in words:
            trie_index = 0
            is_subsequence = True

            for i, char in enumerate(word):
                if char not in trie[trie_index]:
                    is_subsequence = False
                    break
                
                trie_index = trie[trie_index][char] + 1
            
            if is_subsequence:
                subsequence_counter += 1
        
        return subsequence_counter
                
                
                    
                
                
            
                
