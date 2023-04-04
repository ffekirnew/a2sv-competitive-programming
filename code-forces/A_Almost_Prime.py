def unique_factorization(num: int) -> list[int]:
    factorization: int = 0

    d = 2

    while d * d <= num:
        first_d_divisor = True
        while num % d == 0:
            factorization.add(d)
            if first_d_divisor:
                factorization += 1
                first_d_divisor = not first_d_divisor
            num //= d
        d += 1
    
    if num != 1:
        factorization += 1
    
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