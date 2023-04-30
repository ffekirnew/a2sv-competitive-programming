class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        curr_num = 0
        answer = [pref[0]]
        
        for i in range(1, len(pref)):
            curr_num ^= answer[-1]
            answer.append(curr_num ^ pref[i])
            
        return answer
        