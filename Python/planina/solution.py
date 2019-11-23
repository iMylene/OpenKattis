def recursion(a):
    if a==0:
        return 2
    return (recursion(a-1) + recursion(a-1) - 1)

print(recursion(int(input()))**2)