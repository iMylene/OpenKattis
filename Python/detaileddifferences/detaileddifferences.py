''' Assignment: Detailed differences
    Created on 16 april 2016
    @author: Mylene Martodihardjo'''

for i in range(0,input()) :
    string1 = str(raw_input())
    string2 = str(raw_input())
    
    print string1
    print string2

    printhis = ''
    for j in range(0,len(string1)) :
        if string1[j] == string2[j] :
            printhis += '.'
        else :
            printhis += '*'
    print printhis
    print ''