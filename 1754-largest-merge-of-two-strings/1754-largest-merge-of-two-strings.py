class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        word1 = deque(word1)
        word2 = deque(word2)
        
        merge = []
        
        while word1 and word2:
            merge.append(word1.popleft() if word1 > word2 else word2.popleft())
        
        merge.extend(word1)
        merge.extend(word2)
        
        return "".join(merge)
            
            
            
                
            
        
        