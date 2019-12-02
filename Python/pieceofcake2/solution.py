n, h, v = [int(x) for x in input().split()]
thick = 4
cake_list = [h*v*thick, (n-h)*v*thick, h*(n-v)*thick, (n-h)*(n-v)*thick]
print(max(cake_list))