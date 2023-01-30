if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    nums.sort()

    if nums[k] - nums[k - 1]:
        print(nums[k - 1] + 1)
    else:
        print("-1")