N = int(input())
data = []
rank_board = []
rank = 1

for i in range(N):
  data.append(list(map(int, input().split())))

for d1 in data:
  for d2 in data:
    if d1[0] < d2[0] and d1[1] < d2[1]:
      rank += 1
    
  rank_board.append(rank)
  rank = 1
  
for r in rank_board:
    print(r, end = ' ')