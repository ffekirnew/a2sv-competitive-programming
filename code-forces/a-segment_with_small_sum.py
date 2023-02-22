def segment_with_small_sum(nums, size, target):
    longest = 0

    start = 0
    curr_sum = 0

    for end in range(size):
        curr_sum += nums[end]

        while curr_sum > target:
            curr_sum -= nums[start]
            start += 1

        longest = max( longest, end - start + 1 )
    
    return longest


if __name__ == "__main__":
    size, target = map( int, input().split() )
    nums = list( map( int, input().split() ) )

    longest = segment_with_small_sum( nums, size, target )
    print(longest)

    
