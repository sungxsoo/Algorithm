import sys


# DFS: 재귀 호출로 구현
def DFS(v):
    visited[v] = 1
    dfs_result.append(v)
    for i in node[v]:
        if visited[i] == 0:
            DFS(i)


# BFS: 반복문, 큐로 구현
def BFS(v):
    visited[v] = 1
    bfs_result.append(v)
    queue = [v]

    while queue:
        for i in node[queue.pop(0)]:
            if visited[i] == 0:
                visited[i] = 1
                bfs_result.append(i)
                queue.append(i)


# N : 노드의 개수
# M : 간선의 개수
# V : 시작 정점 번호
N, M, V = map(int, sys.stdin.readline().split())

node = [[] for _ in range(N + 1)]

visited = [0 for _ in range(N + 1)]

dfs_result = []
bfs_result = []

# (1,2) 라는 간선이 입력될 때
# 1번 노드에 2 추가
# 2번 노드에 1 추가
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)

# 각 노드 별 연결된 노드에 대한 정렬 (내림차순)
for i in range(N + 1):
    node[i].sort()


# 함수 호출
DFS(V)
# visited 배열 초기화
for i in range(N + 1):
    visited[i] = 0
BFS(V)


# 결과 출력
for i in dfs_result:
    print(i, end=' ')

print()

for i in bfs_result:
    print(i, end=' ')