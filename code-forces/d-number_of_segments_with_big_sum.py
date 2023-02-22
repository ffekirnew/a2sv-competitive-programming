def solve(nums, size, target):
    good_segments = 0

    start = 0
    curr_sum = 0

    for end in range(size):
        curr_sum += nums[end]

        while curr_sum >= target:
            good_segments += size - end
            curr_sum -= nums[start]
            start += 1

    return good_segments


if __name__ == "__main__":
    size, target = map( int, input().split() )
    nums = list( map( int, input().split() ) )

    segs = solve(nums, size, target)
    print(segs)