def unique_factorization(num: int) -> list[int]:
    factorization: set[int] = set()

    d = 2

    while d * d <= num:
        while num % d == 0:
            factorization.add(d)
            num //= d
        d += 1
    
    if num != 1:
        factorization.add(num)
    
    return factorization


def solve():
    num = int(input())
    answer = 0

    for i in range(1, num + 1):
        if len(unique_factorization(i)) == 2:
            answer += 1

    print(answer)


if __name__ == "__main__":
    solve()