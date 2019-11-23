n = int(input())
for i in range(n):
    r, e, c = [int(x) for x in input().split()]
    if r == e - c:
        print("does not matter")
    elif r < e - c:
        print("advertise")
    else:
        print("do not advertise")