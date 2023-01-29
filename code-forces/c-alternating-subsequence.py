if __name__ == "__main__":
    num_tests = int(input())
    answers = []

    for test in range(num_tests):
        length = int( input() )
        arr = list( map( int, input().split() ) )

        answers.append([])

        next_wanted = None # True for positive, False for negative
        curr = None

        for num in arr:
            if next_wanted == None:
                curr = num
                next_wanted = not (num > 0)

            elif next_wanted:
                if num < 0:
                    curr = max(curr, num)
                else:
                    answers[-1].append(curr)
                    curr = num
                    next_wanted = not next_wanted

            else:
                if num > 0:
                    curr = max(curr, num)
                else:
                    answers[-1].append(curr)
                    curr = num
                    next_wanted = not next_wanted

        answers[-1].append(curr)

    for answer in answers:
        print(sum(answer))