height, width, pairs, summation = [], [], [], 0

def height_split(l,d):
    for i in [0,2,4]:
        l.append(d[i])
    return l

def width_split(l,d):
    for i in [1,3,5]:
        l.append(d[i])
    return l

def flip(l,n):
    if n == 1:
        indices = [2]
    elif n == 2:
        indices = [2,4]

    for i in indices:
        temp   = l[i]
        l[i]   = l[i+1]
        l[i+1] = temp
    return l

data = [ int(x) for x in input().split() ]
height = height_split(height,data)
width = width_split(width,data)
#height.append(data[0]), pairs.append(height[i])
#width.append(data[1]), pairs.append(width[i])
summation = [ height[i]*width[i] for i in range(3) ]
sumSquares = summation**(1/2)

if sumSquares == height[0]:
    # can it from a feasable square?
    dif = height[0] - width[0]
    flipped_1 = flip(pairs.copy(),1)
    flipped_2 = flip(pairs.copy(),2)
    print(pairs)
    print(flipped_1)
    print(flipped_2)

    # three rectangles on top of each other  
    if sumSquares == height[1] == height[2] and sumSquares == sum(width):
        print("YES")
    
    # two rectangles on top of each other + one at the side  
    elif height[1] == height[2] and dif == height[1]:
        print("YES")
    #elif height[1] == height[2] and dif == height[1]:
    #    print("YES")

    # two rectangles next to each other + one on top 
    elif sumSquares == height[1] + height[2] and dif == width[1]:
        print("YES")

    else:
        print("NO")
else:
    print("NO")