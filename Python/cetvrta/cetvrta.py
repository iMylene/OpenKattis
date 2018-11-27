''' Assignment: Cetvrta
    Created on 16 april 2016
    @author: Mylene Martodihardjo'''

point1 = raw_input().split(' ')
point2 = raw_input().split(' ')
point3 = raw_input().split(' ')

for i in range(0,2) :
    if point1[i] == point2[i]:
        print point3[i],
    elif point2[i] == point3[i]:
        print point1[i],
    else :
        print point2[i],