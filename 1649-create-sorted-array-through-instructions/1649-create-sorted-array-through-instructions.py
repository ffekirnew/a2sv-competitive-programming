class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        answer = 0
        
        sorted_list = []
        
        for i in range(len(instructions)):
            num = instructions[i]
            
            answer += min( bisect_left(sorted_list, num), len(sorted_list) - bisect_right(sorted_list, num) )
            
            bisect.insort(sorted_list, num)
        
        return answer % (10 ** 9 + 7)
    