import math
a, i = [int(x) for x in input().split()]
new_i = i - .99

print(math.ceil(a*new_i))