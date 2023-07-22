if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = sorted(list(map(int, input().split())))

    if not k:
        ans = nums[0] - 1
    else:
        ans = nums[k - 1]
    
    print(nums)
    print(ans)

    count = 0
    for i in range(n):
        if nums[i] <= ans:
            count += 1
    
    if count != k or not (1 <= ans <= 1_000_000_000):
        print(-1)
    else:
        print(ans)
    
    exit()



    

