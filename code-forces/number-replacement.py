def main():
    n_test_cases = int(input())
    answers = []
    for test_case in range(n_test_cases):
        # accept in inputs
        test_case_length = int(input())
        number_list = map(int, input().split())
        letter_string = input()

        # create a dictionary to know which number is being changed to which charachter
        mapping_dict = {}
        # to know if differences are found
        flag = True
        for idx, number in enumerate(number_list):
            if number in mapping_dict:
                if mapping_dict[number] != letter_string[idx]:
                    flag = False
                    break
            mapping_dict[number] = letter_string[idx]
        answers.append("YES" if flag else "NO")
    for answer in answers:
        print(answer)

if __name__ == "__main__":
    main()
