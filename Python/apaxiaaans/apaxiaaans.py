''' Assignment: Apaxiaaaaaaaaaaaans
    Created on 16 april 2016
    @author: Mylene Martodihardjo'''

import sys

singleName = raw_input()
sys.stdout.write(singleName[0])
for i in range(1,len(singleName)) :
    if singleName[i] != singleName[i-1] :
        sys.stdout.write(singleName[i])