total = int(input())
number = [int(x) for x in input().split()]
sum = 0

for i in range(total):
    if number[i] < 0:
        sum = sum + number[i]
print(-1*sum)