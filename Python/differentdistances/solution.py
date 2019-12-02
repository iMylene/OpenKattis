import sys
data = sys.stdin.readlines()

for x in range(len(data) - 1):
    x1, y1, x2, y2, p = [ float(y) for y in data[x].split() ]
    print("{0:.10f}".format((abs(x1 - x2)**p + abs(y1 - y2)**p)**(1/p)))