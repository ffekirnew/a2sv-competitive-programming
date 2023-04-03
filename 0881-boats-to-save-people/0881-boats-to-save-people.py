class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        answer = 0
        
        # sort the people
        people.sort()
        
        # set up two pointers
        left, right = 0, len(people) - 1
        
        # loop through he people and match the heaviest and the lightest
        while left <= right:
            if left < right:
                curr = people[left] + people[right]
            else:
                curr = people[left]
                
            if curr > limit:
                answer += 1
                right -= 1

            elif curr <= limit:
                answer += 1
                right -= 1
                left += 1

        return answer