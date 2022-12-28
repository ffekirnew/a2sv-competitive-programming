from collections import defaultdict
def main():
    # create the object to be returned
    answer = defaultdict(list)
    # accept the inputs
    n, m = map(int, input().split())
    group_a = []
    for iterator in range(n):
        group_a.append(input())
    group_b = []
    for iterator in range(m):
        group_b.append(input())
    # transform group into word:occurence_index dictionary
    group_a_dict = defaultdict(list)
    for idx, word in enumerate(group_a):
        group_a_dict[word].append(idx + 1)
    # print the results
    for word in group_b:
        if word in group_a_dict:
            print(*group_a_dict[word])
        else:
            print(-1)

if __name__ == "__main__":
    main()
