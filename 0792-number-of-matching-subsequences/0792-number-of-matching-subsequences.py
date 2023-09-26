class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Build a trie for the string
        trie = [None for __ in range(len(s) + 1)]
        for i in range(len(s) - 1, -2, -1):
            if i == len(s) - 1:
                trie[i + 1] = [ None for _ in range(26) ]
            else:
                new_trie_node = trie[i + 2].copy()
                new_trie_node[ord(s[i + 1]) - 97] = i + 1

                trie[i + 1] = new_trie_node

        # Go through the words and count the subsequences
        subsequences = 0

        for word in words:
            trie_index = 0
            is_subsequence = True

            for i, char in enumerate(word):
                char_index = ord(char) - 97
                if trie[trie_index][char_index] == None:
                    is_subsequence = False
                    break
                
                trie_index = trie[trie_index][char_index] + 1
            
            if is_subsequence:
                subsequences += 1
        
        return subsequences
                
                
                    
                
                
            
                
