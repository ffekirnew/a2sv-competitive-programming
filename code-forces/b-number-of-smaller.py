result = []

n, m = list(map(int, input().split()))

arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

idx = 0
for num in arr_2:
    while idx < n and arr_1[idx] < num:
        idx += 1
    
    result.append(idx)

print(*result)