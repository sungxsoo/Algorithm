N, K = map(int, input().split())

M = []
count = 0

for x in range(N):
    M.append(int(input()))

M.sort(reverse=True)

for m in M:
  count += K // m
  K %= m

print(count)