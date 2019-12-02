x = int(input())

for i in range(x):
    b, p = [float(x) for x in input().split()]
    print("{0:.4f}".format((60*(b-1))/p), "{0:.4f}".format((60*b)/p), "{0:.4f}".format((60*(b+1))/p))