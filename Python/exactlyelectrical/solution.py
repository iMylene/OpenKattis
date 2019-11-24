start_x, start_y = [int(x) for x in input().split()]
end_x, end_y = [int(x) for x in input().split()]

battery = int(input())
distance = abs(start_x - end_x) + abs(start_y - end_y)
rest = battery - distance

if distance > battery:
    print("N")
elif rest % 2 == 0:
    print("Y")
else:
    print("N")