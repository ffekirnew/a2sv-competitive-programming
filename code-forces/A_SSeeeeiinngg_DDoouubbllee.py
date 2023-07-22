def solve():
    tests = int(input())
    for _ in range(tests):
        word = input()
        copy_word = word[::-1]
        print(word + copy_word)

if __name__ == "__main__":
    solve()