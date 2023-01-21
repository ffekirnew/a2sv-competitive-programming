def main():
    number_of_test_cases = int(input())

    for test in range(number_of_test_cases):
        rows, cols = map(int, input().split())
        board = []
        for row in range(rows):
            row_input = map(int, input().split())
            board.append(list(row_input))
        print(board)





if __name__ == "__main__":
    main()