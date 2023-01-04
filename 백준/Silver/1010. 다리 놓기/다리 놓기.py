import math

T = int(input())
data = []
answ = []

for i in range(T):
  data.append(list(map(int, input().split())))

for d in data:
  answ.append(math.comb(d[1], d[0]))


for a in answ:
  print(a, end=' ')