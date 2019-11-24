import sys
data = [int(x) for x in sys.stdin.readlines()[1:]]

for number in data:
    #print(number)
    # Bepaal de set van alle getallen (range(0,2**6))
    totalSet = set(range(2**number))
    # haal daar voor i in range(2,6) getallen vanaf...
    removeSet = set()
    for i in range(2,number+1):
        removeSet = removeSet.union(set(range(3*2**(i-2),2**number,2**i)))
        if i>3:
            for j in range(1,2**(i-2)):#range(1,2**i-3):
                #print(removeSet.intersection(set(range(3*2**(i-2)+j,2**(i-2)-1,2**i))))
                #print(removeSet.intersection(set(range(3*2**(i-2)+j,2**(i-2)-1,2**i))))
                removeSet = removeSet.union(set(range(3*2**(i-2)+j,2**i+2**(i-2)-1,2**i)))
    totalSet = totalSet - removeSet
    #print(totalSet)
    # Kijk dan voor alle getallen of ze idd geen '11' bevatten (dus de overige getallen)
    for item in totalSet:
        if '11' in format(item, "b"):
            print('missing: {}'.format(item))
    #for item in removeSet:
    #    if '11' not in format(item, "b"):
    #        print('to much: {}'.format(item))
    #
    # Als dat klopt dan doe je... 2**6-sum([len(foroutkomst) for x in range(2,6)])
    #print( ( (2**number)-len(removeSet) )%10**9+7)
    print( ( (2**number)-len(removeSet) )%(10**9+7))


    64
    1000000
    1001100
    0101100

    0001100
    1101100