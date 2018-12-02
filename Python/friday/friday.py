''' Assignment: Friday the 13th
    Created on 2018-12-01
    @author: Michael Vasseur, Mylene Martodihardjo'''

import sys

data  = sys.stdin.readlines()
cases = int(data[0])

for case in range(cases):
    day_counter     = 0
    friday13th      = 0
    friday_offset   = 5 # each year starts a Sunday
    
    total_days      = int(data[2*case + 1].split(" ")[0])
    possible_days   = [ x for x in range(total_days) if x%7 == friday_offset ]
    days_in_months  = [ int(x) for x in data[2*case + 2].split(" ") ]

    for dmi in days_in_months:
        if dmi>=13:
            if day_counter+12 in possible_days:
                friday13th +=1
        day_counter += dmi
    
    print(friday13th)