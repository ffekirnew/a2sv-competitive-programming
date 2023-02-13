class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] * len(arr2)
        
        for i, num in enumerate(arr2):
            for num2 in arr1:
                if num == num2:
                    count[i] += 1
                    
        answer = []
        
        for i, c in enumerate(count):
            for j in range(c):
                answer.append(arr2[i])
        
        other = []
        for num in arr1:
            if num not in arr2:
                other.append(num)
        other.sort()
        
        answer.extend(other)
        return answer
        