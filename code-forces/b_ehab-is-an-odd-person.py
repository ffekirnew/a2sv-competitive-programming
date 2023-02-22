if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(n):
        for j in range(i, n):
            if ( nums[i] + nums[j] ) % 2 and nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                break
    
    print(*nums)
    
