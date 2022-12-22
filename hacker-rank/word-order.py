from collections import Counter
if __name__ == "__main__":
    n = int(input())
    words = list()
    freq = dict()
    for i in range(n):
        words.append(input())
    freq = Counter(words)
    print(len(freq))
    print(*freq.values())
