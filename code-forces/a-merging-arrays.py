if __name__ == "__main__":
    result = []

    n, m = map(int, input().split())
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))

    arr_1_ptr, arr_2_ptr = 0, 0

    while arr_1_ptr < n or arr_2_ptr < m:
        if arr_1_ptr == n:
            result.append(arr_2[arr_2_ptr])
            arr_2_ptr += 1

        elif arr_2_ptr == m:
            result.append(arr_1[arr_1_ptr])
            arr_1_ptr += 1

        else:
            if arr_1[arr_1_ptr] < arr_2[arr_2_ptr]:
                result.append(arr_1[arr_1_ptr])
                arr_1_ptr += 1

            else:
                result.append(arr_2[arr_2_ptr])
                arr_2_ptr += 1

    print(*result)
