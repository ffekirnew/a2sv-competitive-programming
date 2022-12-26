import textwrap

def wrap(string, max_width):
    # create the object to be returned
    answer = []
    char_index = 0
    # loop through the string
    while char_index < len(string):
        if char_index != 0 and (char_index) % max_width == 0:
            answer.append("\n")
        answer.append(string[char_index])
        char_index += 1
    # return the solution
    return "".join(answer)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)