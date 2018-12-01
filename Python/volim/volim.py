''' Assignment: Volim
    Created on 2018-12-01
    @author: Mylene Martodihardjo'''

import sys

total_time  = 3*60 + 30
data        = sys.stdin.readlines()
person      = int(data[0])
questions   = range(int(data[1]))
print(" ")
for i in questions:
    time   = int(data[i+2].split(" ")[0])
    answer = data[i+2].split(" ")[1]
    total_time -= time
    
    if (total_time <= 0):
        print(person)
        exit()
    elif ("T" in answer):
        if (person == 8):
            person = 1
        else:
            person += 1