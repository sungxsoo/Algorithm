import sys
from collections import deque

N = int(sys.stdin.readline())

graph = []
area_num = []

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def find_height_range(graph):
  min_height = min(map(min, graph))
  max_height = max(map(max, graph))
  return min_height, max_height

def convert_graph(H, graph):
  new_graph = []
  for i in range(N):
    row = []
    for j in range(N):
      if graph[i][j] > H:
        row.append(1)
      else:
        row.append(0)
    new_graph.append(row)
  return new_graph
  

def BFS(a,b):
  queue = deque()
  new_graph[a][b] = 0
  queue.append((a,b))
  
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny <0 or ny >= N:
        continue
      if new_graph[nx][ny] == 0:
        continue
      if new_graph[nx][ny] == 1:
        new_graph[nx][ny] = 0
        queue.append((nx,ny))
  return 1
  


for i in range(N):
  graph.append(list(map(int, sys.stdin.readline().split())))


min_height, max_height = find_height_range(graph)

for i in range(min_height, max_height):
  new_graph = convert_graph(i, graph)
  area_count = 0
  for i in range(N):
    for j in range(N):
      if new_graph[i][j] == 1:
        area_count+=BFS(i,j)
  area_num.append(area_count)

if len(area_num) == 0:
  print(1)
else:
  print(max(area_num))

