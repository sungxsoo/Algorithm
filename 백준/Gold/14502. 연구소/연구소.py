from itertools import combinations
import copy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus_spread(v, temp):
    for i in range(4):
        nx = v[0] + dx[i]
        ny = v[1] + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus_spread([nx, ny], temp)

def count_safe_area(temp):
    count = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                count += 1
    return count

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
possible_wall = []
virus = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            possible_wall.append([i, j])
        elif lab[i][j] == 2:
            virus.append([i, j])

walls = list(combinations(possible_wall, 3))
max_area = 0

for wall in walls:
    temp = copy.deepcopy(lab)
    for w in wall:
        temp[w[0]][w[1]] = 1

    for v in virus:
        virus_spread(v, temp)

    max_area = max(max_area, count_safe_area(temp))

print(max_area)
