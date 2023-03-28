import sys
from collections import deque


def BFS(a, b):
  queue = deque()
  queue.append(a)
  while queue:
    me = queue.popleft()
    for i in graph[me]:
      if chon_su[i] == 0:
        chon_su[i] = chon_su[me] + 1
        queue.append(i)


N = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
chon_su = [0 for _ in range(N + 1)]

for i in range(M):
  x, y = map(int, sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)

BFS(a, b)

if chon_su[b] == 0:
  print(-1)
else:
  print(chon_su[b])
  
