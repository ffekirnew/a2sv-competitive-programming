class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # do counting sort
        
        max_height = max(heights)
        
        counter = [[] for i in range(max_height)]
        
        for i in range(len(heights)):
            counter[heights[i] - 1].append(names[i])
        
        answer = []
        
        for count in reversed(counter):
            answer.extend(count)
        
        return answer