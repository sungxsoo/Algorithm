from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for i in range(n):
    city = list(map(int, input().split()))
    for j in range(n):
        if city[j] == 1:
            house.append((i, j))
        elif city[j] == 2:
            chicken.append((i, j))

minv = float('inf')
for ch in combinations(chicken, m):
    sumv = 0
    for home in house:
        sumv += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
        if minv <= sumv: break
    if(sumv < minv): minv = sumv

print(minv)
