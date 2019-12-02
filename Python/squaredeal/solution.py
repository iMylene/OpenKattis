height, width, summation = [], [], 0

for i in range(3):
    data = [ int(x) for x in input().split() ]
    height.append(data[0]), width.append(data[1])
    summation += height[i]*width[i]
sumSquares = summation**(1/2)

if sumSquares == height[0]:
    # can it from a feasable square?
    dif = height[0] - width[0]
    
    # three rectangles on top of each other  
    if sumSquares == height[1] == height[2] and sumSquares == sum(width):
        print("YES")
    
    # two rectangles on top of each other + one at the side  
    elif height[1] == height[2] and sumSquares == sum(height[1:3]):
        print("YES")

    # two rectangles next to each other + one on top 
    elif sumSquares == height[1] + height[2]:
        print("YES")

    else:
        print("NO")
else:
    print("NO")