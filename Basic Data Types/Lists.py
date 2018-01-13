if __name__ == '__main__':
    L = []
    N = int(input())
    for _ in range(N):
        input_string = input().split()
        # The input will consist of a command first, followed by the arguments
        command = input_string[0]
        arguments = input_string[1:]
        if (command != "print"):
            command += "("+ ",".join(arguments) +")"
            eval("L." + command)
        else:
            print(L)
