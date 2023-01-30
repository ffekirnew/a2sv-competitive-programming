num_tests = int(input())
answers = []  

for test in range(num_tests):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    used = 0

    for idx in range(n - 1):
        if arr[idx + 1] - arr[idx] <= 1:
            used += 1

    if n - used <= 1:
        answers.append("YES")
    else:
        answers.append("NO")

for ans in answers:
    print(ans)