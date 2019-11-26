import datetime
d, m = [int(x) for x in input().split()]

print(datetime.datetime(2009, m, d).strftime("%A"))