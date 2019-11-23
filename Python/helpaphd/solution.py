import sys
data = sys.stdin.readlines()

for i in range(1,len(data)):
    if "P=NP" in data[i]:
        print("skipped")
    else:
        print(sum([int(x) for x in data[i].split("+")]))