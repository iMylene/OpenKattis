''' Assignment: Quality-Adjusted Life-Year
    Created on 29 november 2018
    @author: Mylene Martodihardjo'''

import sys

result = 0
data = sys.stdin.readlines()
for i in range(int(data[0])):
    quality,age = [ float(x) for x in data[i+1].split(" ") ]
    result += quality * age
print(result)