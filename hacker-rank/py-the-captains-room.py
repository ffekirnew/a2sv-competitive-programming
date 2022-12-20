from collections import Counter
if __name__ == "__main__":
    k = int(input())
    room_numbers = input().split(" ")
    groups = Counter(room_numbers)
    for key in groups.keys():
        if groups[key] == 1:
            print(key)