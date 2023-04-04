def solve():
    n = int(input())

    print("NO" if n % 3 == 0 or n % 5 == 0 else "YES")

if __name__ == "__main__":
    solve()