import sys

infected_virus = []

def BFS(v):
  infected[v] = 1
  infected_virus.append(v)
  for i in virus[v]:
    if infected[i] == 0:
      BFS(i)

# 바이러스 수
N = int(sys.stdin.readline())
# 네트워크 수
M = int(sys.stdin.readline())

virus = [[] for _ in range(N+1)]
infected = [0 for _ in range(N+1)]

for i in range(M):
  a,b = map(int, sys.stdin.readline().split())
  virus[a].append(b)
  virus[b].append(a)

BFS(1)

print(len(infected_virus)-1)