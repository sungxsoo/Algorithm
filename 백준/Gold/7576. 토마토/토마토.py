from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                queue.append([nx, ny])
                box[nx][ny] = box[x][y] + 1

m, n = map(int, input().split())
box, queue = [], deque()

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            queue.append([i, j])
    box.append(row)

bfs()

days = max([max(row) for row in box]) - 1 # 날짜는 1부터 시작하므로 1을 뺀다.
unripe = any(0 in row for row in box) # 익지 않은 토마토가 있으면 True, 없으면 False

if unripe: print(-1)
else: print(days)
