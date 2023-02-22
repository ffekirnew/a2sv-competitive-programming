def segment_with_big_sum(nums, size, target):
    shortest = float('inf')

    start = 0
    curr_sum = 0

    for end in range(size):
        curr_sum += nums[end]

        while curr_sum >= target:
            shortest = min( shortest, end - start + 1 )
            curr_sum -= nums[start]
            start += 1

    
    return shortest if shortest != float('inf') else -1


if __name__ == "__main__":
    size, target = map( int, input().split() )
    nums = list( map( int, input().split() ) )

    shortest = segment_with_big_sum( nums, size, target )
    print(shortest)

    
