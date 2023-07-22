def solve():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        a = list(map(int, input().split()))
        a_prime = list(map(int, input().split()))

        # find the longest sorted
        answer = []
        max_length = 0
        l = 0
        for r in range(1, n):
            if a_prime[r - 1] > a_prime[r]:
                l = r
            
            if r - l + 1 > max_length:
                max_length = r - l + 1
                answer = [l + 1, r + 1]
        
        print(*answer)

if __name__ == "__main__":
    solve()