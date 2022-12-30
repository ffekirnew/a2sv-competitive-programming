class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # create the object to be returned
        answer = []
        # calculate the sum of the evens before hand to manipulate later
        sum_of_evens = sum([num for num in nums if num % 2 == 0])
        # loop through the queries and perform the operations
        for query in queries:
            if nums[query[1]] % 2 == 0:
                sum_of_evens -= nums[query[1]]
                
            nums[query[1]] += query[0]
            
            if nums[query[1]] % 2 == 0:
                sum_of_evens += nums[query[1]]

            answer.append(sum_of_evens)
        # return the solution
        return answer
        
        