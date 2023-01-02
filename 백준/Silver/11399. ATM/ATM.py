N = int(input())
P = list(map(int, input().split()))

P.sort(reverse = True)

time = 0

for index, value in enumerate(P):
    time += value * (index+1)

print(time)