if __name__ == '__main__':
    N = int(input())
    array_list = []
    for i in range(N):
        command = input().split()
        opcode = command[0]
        if opcode == "insert":
            array_list.insert(int(command[1]), int(command[2]))
        elif opcode == "remove":
            array_list.remove(int(command[1]))
        elif opcode == "print":
            print(array_list)
        elif opcode == "append":
            array_list.append(int(command[1]))
        elif opcode == "sort":
            array_list.sort()
        elif opcode == "pop":
            array_list.pop()
        elif opcode == "reverse":
            array_list.reverse()
