def main():
    # take in inputs
    num_english_subscribers = int(input())
    english_subscribers = set([student for student in input().split()])
    num_french_subscribers = int(input())
    french_subscribers = set([student for student in input().split()])
    # print the solution
    print(len(english_subscribers.union(french_subscribers)))

    
if __name__ == "__main__":
    main()