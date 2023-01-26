class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        
        merge = []
        
        while word1 and word2:
            merge.append(word1.pop(0) if word1 > word2 else word2.pop(0))
        
        merge.extend(word1)
        merge.extend(word2)
        
        return "".join(merge)
            
            
            
                
            
        
        