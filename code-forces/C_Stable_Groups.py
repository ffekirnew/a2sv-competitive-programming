import math


def solve():
    n, k, x = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    nums.sort()

    partitions = [[]]
    answer = 1

    for num in nums:
        if partitions[-1] and num - partitions[-1][-1] > x:
            partitions.append([])
            answer += 1

        partitions[-1].append(num)
    
    answer = len(partitions)

    differences = []

    for i in range(1, len(partitions)):
        differences.append(partitions[i][0] - partitions[i - 1][-1])
    
    differences.sort(reverse=True)

    while differences:
        diff = differences.pop()

        if k and diff / 2 <= x:
            answer -= 1
            k -= 1
        else:
            students_needed = math.ceil((diff / 2) / x)

            if k >= students_needed:
                answer -= 1
                k -= students_needed

    print(answer)

if __name__ == "__main__":
    solve()