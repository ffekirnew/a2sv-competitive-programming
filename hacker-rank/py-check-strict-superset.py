# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    answer = True
    
    A = set(input().split())
    N = int(input())
    for i in range(N):
        B = set(input().split())
        if B.difference(A) or not A.difference(B):
            answer = False
            break
    print(answer)
