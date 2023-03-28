import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def BFS(a, b):
  queue = deque()
  queue.append((a, b))
  graph[a][b] = 0
  count = 1

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= N or ny >= N:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        count += 1
        queue.append((nx, ny))

  return count


N = int(sys.stdin.readline())

graph = []

for i in range(N):
  graph.append(list(map(int, input())))

total_virus = []

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      num_virus = BFS(i, j)
      total_virus.append(num_virus)

total_virus.sort()

print(len(total_virus))
for i in total_virus:
  print(i)


