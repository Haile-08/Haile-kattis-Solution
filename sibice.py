import math
l = [int(x) for x in input().split()]
c = math.sqrt(l[1]**2 + l[2]**2)
for y in range(l[0]):
    p = int(input())
    if p <= c:
        print('DA')
    else:
        print('NE')
