import sys
from collections import deque

visited = [0 for _ in range(100001)]

def BFS(N, K):
  q = deque([(N,0)])
  visited[N] = 1
  while q:
    num, cnt = q.popleft()
    if num == K:
      return cnt 
    
    for i in (num*2, num+1, num-1):
      if 0<= i <= 100000:
        if not visited[i]:
          visited[i] = 1
          q.append((i,cnt+1))

N, K = map(int, sys.stdin.readline().split())
print(BFS(N,K))