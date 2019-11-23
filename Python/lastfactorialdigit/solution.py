import sys
n, data = int(input()), [int(x) for x in sys.stdin.readlines()]
returnitself = [1, 2, 4]
for i in range(n):
    if data[i] in returnitself:
        print(data[i])
    elif data[i] == 3:
        print("6")
    else:
        print("0")