from collections import defaultdict


def unique_segments(nums, size, target):
    segments = 0

    start = 0
    unique = defaultdict(int)

    for end in range(size):
        unique[nums[end]] += 1

        while len(unique) > target:
            if unique[nums[start]] == 1: del unique[nums[start]]
            else: unique[nums[start]] -= 1
            start += 1
        
        segments += end - start + 1

    return segments


if __name__ == "__main__":
    size, target = map( int, input().split() )
    nums = list( map( int, input().split() ) )

    segments = unique_segments( nums, size, target )
    print(segments)

    
