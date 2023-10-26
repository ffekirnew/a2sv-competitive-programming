class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        count = 0
        
        arr.sort()

        nums = set(arr)
        count_rooted_at = {num: 1 for num in arr}
        
        for i, root in enumerate(arr):
            seen = set([])

            for j in range(i):
                child = arr[j]
                if child in seen or root % child != 0:
                    continue

                other_child = root // child

                if other_child in nums:
                    seen.add(child)
                    seen.add(other_child)
                    
                    factor = 1 if child == other_child else 2

                    count_rooted_at[root] += (
                        factor *
                        count_rooted_at[child] *
                        count_rooted_at[other_child]
                    )
            
            count += count_rooted_at[root]
        
        return count % (10 ** 9 + 7)
            
        