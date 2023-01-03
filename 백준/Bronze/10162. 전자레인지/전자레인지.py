T = int(input())
time = [300,60,10]
answer = []
count = 0

for t in time:
    count = T // t
    answer.append(count)
    T %= t
    count = 0  
    
if T==0:
    for a in answer:
      print(a, end=' ')
else:
    print(-1)