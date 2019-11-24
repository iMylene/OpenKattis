import sys
data = [int(x) for x in sys.stdin.readlines()[1:]]

def cleanup(n):
    not_check = set()
    if n>1:
        oft = n//2
        start = 2**n-1
        stop = 2**n-1
        for i in range(oft):
            stop -= 2**(n-(i+1)*2)
        not_check = set(range(start,stop,-1))
        #print(not_check)
        
    #else:
    #    return set([3])


    return not_check

for number in data:
    #print(countBinaries(number) % (10**9+7))
    bad_numbers = set()#set(range(2**number))
    for i in range(number):
        bad_numbers = bad_numbers.union(cleanup(i+1))
    bad_numbers = bad_numbers.union(set([2**i+3 for i in range(2,number)]))
    bad_numbers = bad_numbers.union(set([2**i+7 for i in range(2,number)]))
    bad_numbers = bad_numbers.union(set([2**i+11 for i in range(2,number)]))
    counter = 0
    for item in set(range(2**number))-bad_numbers:
        #if item in bad_numbers:
        #    continue
        #check_numbers:
        if '11' in "{0:b}".format(item):
            print("{0:b} {0:d}".format(item))
        if '11' not in "{0:b}".format(item):
            counter +=1
    #print
    print(counter%(10**9+7))