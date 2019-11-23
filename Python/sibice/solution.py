_, width, height = [int(x) for x in (input().split())]
diagonal = (width**2 + height**2)**(.5)

import sys
matches = [int(x) for x in sys.stdin.readlines()]

for match in matches:
    if match > diagonal:
        print("NE")
    else:
        print("DA")