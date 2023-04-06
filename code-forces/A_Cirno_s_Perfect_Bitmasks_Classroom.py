def solve():
    tests = int(input())
    for _ in range(tests):
        x = int(input())
        x_copy = x

        smallest = None
        curr_bit = 0
        to_be_added = 0

        while x:
            if x % 2:
                smallest = 2 ** curr_bit
                break
            x >>= 1
            curr_bit += 1
        
        if smallest is x_copy:
            curr_bit = 0
            while not to_be_added:
                if x_copy % 2 == 0:
                    to_be_added = 2 ** curr_bit
                    break
                x_copy >>= 1
                curr_bit += 1
        
        print(smallest + to_be_added)



if __name__ == "__main__":
    solve()
