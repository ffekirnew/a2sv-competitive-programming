from collections import deque
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        side_lengths = deque([int(i) for i in input().split()])
        print(side_lengths)
        stack = []
        while side_lengths:
            if side_lengths[0] > side_lengths[-1]:
                if stack and side_lengths[0] > stack[-1]:
                    break
                stack.append(side_lengths.popleft())
            else:
                if stack and side_lengths[-1] > stack[-1]:
                    break
                stack.append(side_lengths.pop())
        print("No" if side_lengths else "Yes")