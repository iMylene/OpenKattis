from statistics import mean
ga1, gb1, ga2, gb2 = [int(x) for x in input().split()] 
ea1, eb1, ea2, eb2 = [int(x) for x in input().split()]

gunnar = sum( [ mean([x for x in range(ga1,gb1)]), mean([x for x in range(ga2,gb2)]) ] )
emma = sum ( [ mean([x for x in range(ea1,eb1)]), mean([x for x in range(ea2,eb2)]) ] )

if gunnar == emma:
    print('Tie')
elif gunnar > emma:
    print('Gunnar')
else:
    print('Emma')