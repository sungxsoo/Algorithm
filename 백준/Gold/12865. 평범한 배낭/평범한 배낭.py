import sys
N,K = map(int, sys.stdin.readline().split())

items = [[0,0]]

knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    items.append(list(map(int, sys.stdin.readline().split())))


for i in range(1, N+1):
    for j in range(1, K+1):
        w = items[i][0]
        v = items[i][1]

        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(v + knapsack[i-1][j-w], knapsack[i-1][j])

print(knapsack[N][K])
