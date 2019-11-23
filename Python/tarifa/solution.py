import sys
max_megabytes, n, data = int(input()), int(input()), [int(x) for x in sys.stdin.readlines()]
used = sum(data)
print(n*max_megabytes - used + max_megabytes)