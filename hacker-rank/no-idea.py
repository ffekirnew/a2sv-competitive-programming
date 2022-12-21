if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]
    arr = [j for j in input().split()]
    like_set = set([k for k in input().split()])
    dislike_set = set([k for k in input().split()])
    happiness = 0
    for i in range(n):
        if arr[i] in like_set:
            happiness += 1
        elif arr[i] in dislike_set:
            happiness -= 1
    print(happiness)
