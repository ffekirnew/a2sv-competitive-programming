import sys
import threading

def solve():
    tests = int(input())
    for _ in range(tests):
        start, target = list(map(int, input().split()))

        is_separable_cache = {}
        def is_separable(n):
            if n not in is_separable_cache:
                is_separable_cache[n] = n % 3 == 0
            return is_separable_cache[n]

        memo = {}
        def top_down(n):
            if n == target:
                return True

            if not is_separable(n):
                return False
            
            if n not in memo:
                memo[n] = top_down(n // 3) or top_down((n // 3) * 2)
            
            return memo[n]

        print("YES" if top_down(start) else "NO")


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
solution_thread = threading.Thread(target = solve)
solution_thread.start()
solution_thread.join()
