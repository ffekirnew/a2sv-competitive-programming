def swap_case(s):
    answer = []
    for c in s:
        if 64 < ord(c) < 91:
            answer.append(chr(ord(c) + 32))
        elif 96 < ord(c) < 123:
            answer.append(chr(ord(c) - 32))
        else:
            answer.append(c)
    return "".join(answer)

if __name__ == '__main__':