p = int(input())
l = [int(x) for x in input().split()]
sum = 0
for i in range(len(l)):
    if l[i] < 0:
       sum += l[i]
print(abs(sum))
