# a global variable to follow to compare t-shirt sizes
tshirt_sizes = {'S' : -1, 'M' : 0, 'L' : 1}

def tshirt_size(tshirt):
    '''Generates a number t-shirt size
    '''
    size = 1
    for letter in tshirt:
        size *= 10 if (letter == 'X') else tshirt_sizes[letter]
    return size


def main():
    # take in the first input
    number_of_test_cases = int(input())
    # create an array to contain all answers and print later on
    answers = []

    # take in the test cases and generate the solutions
    for test_case in range(number_of_test_cases):
        # take in input
        tshirt_1, tshirt_2 = input().split()

        # generate sizes values in numbers to compare
        size_1 = tshirt_size(tshirt_1)
        size_2 = tshirt_size(tshirt_2)

        # record the answer
        answers.append('<' if (size_1 < size_2) else '=' if (size_1 == size_2) else '>')
    
    # print the answers
    for answer in answers:
        print(answer)
        


if __name__ == "__main__":
    main()
