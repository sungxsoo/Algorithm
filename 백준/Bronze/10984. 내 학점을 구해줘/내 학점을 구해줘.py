T = int(input())

for i in range(T):
  sum = 0
  rate = 0
  N = int(input())
  for j in range(N):
    a, b = input().rstrip().split()
    a = int(a)
    b = float(b)
    rate += a
    sum += a * b
  print(rate, end=' ')
  print(round(sum / rate, 1))
