if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    if all(num % 2 for num in nums) or all(num % 2 == 0 for num in nums):
        print(*nums)
    else:
        print(*sorted(nums))
    
