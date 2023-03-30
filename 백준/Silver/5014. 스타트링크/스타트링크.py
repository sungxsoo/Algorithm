import sys
from collections import deque


def BFS(S):
  queue = deque([S])
  visited[S] = 1
  
  while queue:
    f = queue.popleft()
    if f == G:
      return count[G]
    for i in climbing:
      nf = f + i
      if nf>0 and nf<=F:
        if visited[nf]==0:
          count[nf] = count[f] + 1
          visited[nf] = 1
          queue.append(nf)
  if count[G] == 0:
        return "use the stairs"


F, S, G, U, D = map(int, sys.stdin.readline().split())

climbing = [U, -1*D]

count = [0 for _ in range(F + 1)]
visited = [0 for _ in range(F + 1)]

print(BFS(S))