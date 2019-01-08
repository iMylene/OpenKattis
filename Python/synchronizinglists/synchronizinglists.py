''' Assignment: Synchronizing Lists
    Created on 2018-12-02
    @author: Michael Vasseur, Mylene Martodihardjo'''

import sys
data = sys.stdin.readlines()
c = 0
st=0
while "0" not in data[c]:
    if st!=0:
        print("")
    loop = int(data[c])
    lista = [ int(data[c+1+i]) for i in range(loop) ]
    listb = [ int(data[c+1+i+loop]) for i in range(loop) ]
    listp = listb.copy()
    
    slista = sorted(lista)
    slistb = sorted(listb)
    
    for i in range(loop):
        id = lista.index(slista[i])
        print("id:",id)
        listp[id] = slistb[i]
    for i in listp:
        print(i)
    c += 2*loop+1
    st=1