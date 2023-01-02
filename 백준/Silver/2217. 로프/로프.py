N = int(input())
val = []
max = 0

for x in range(N):
  val.append(int(input()))

val.sort(reverse=True)

for index in range(N):
  new = val[index] * (index+1)
  if(max < new):
    max = new

print(max)