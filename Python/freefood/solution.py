y = int(input())
freeFoodDays = set()

for x in range(y):
    begin, end = [ int(x) for x in input().split() ]
    days = [ x for x in range(begin, end + 1) ]
    [ freeFoodDays.add(x) for x in days ]
print(len(freeFoodDays))