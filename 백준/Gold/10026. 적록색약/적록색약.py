dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, arr, visited):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
                stack.append((nx, ny))


n = int(input().rstrip())
arr1 = [list(input().rstrip()) for _ in range(n)]
arr2 = [['R' if color=='G' else color for color in row] for row in arr1]

visited1 = [[False]*n for _ in range(n)]
visited2 = [[False]*n for _ in range(n)]

normal = rg_weakness = 0

for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            dfs(i, j, arr1, visited1)
            normal += 1
        if not visited2[i][j]:
            dfs(i, j, arr2, visited2)
            rg_weakness += 1

print(normal, rg_weakness)
