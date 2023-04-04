if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    nums.sort()

    if not k:
        print(nums[0] - 1)
    else:
        answer = nums[k] - 1
        less_count = 0

        for i in range(k):
            if nums[i] <= answer:
                less_count += 1
            
        if answer < 1 or less_count != k:
            print("-1")
            exit()
        
        print(answer)