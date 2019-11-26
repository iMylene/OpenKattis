import sys
data = [int(x) for x in sys.stdin.readlines()[1:]]

storage = {}

def fib(n):
    n1, n2 = 2, 3
    global storage
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        if n-1 not in storage.keys():
            storage[n-1] = fib(n-1)
        if n-2 not in storage.keys():
            storage[n-2] = fib(n-2)
        return storage[n-1]+storage[n-2]

for number in data:
    print(fib(number)%( (10**9)+7) )