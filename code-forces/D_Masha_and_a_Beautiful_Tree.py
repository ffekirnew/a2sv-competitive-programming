def merge(left, right, count=0):
    i, j = 0, 0
    merged = []
    counted = False

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            if j:
                return False, None
            merged.append(left[i])
            i += 1
        else:
            if i:
                return False, None
            if not counted:
                count += 1
                counted = True
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged, count

def merge_sort(nums):
    if len(nums) < 2:
        return nums, 0
    
    mid = len(nums) // 2

    left, left_count = merge_sort(nums[:mid])
    right, right_count = merge_sort(nums[mid:])

    if left and right:
        return merge(left, right, left_count + right_count)
    
    return False, None

tests = int(input())
for _ in range(tests):
    n = int(input())
    nums = list(map(int, input().split()))

    can_be_sorted, count = merge_sort(nums)

    if can_be_sorted:
        print(count)
    else:
        print("-1")
