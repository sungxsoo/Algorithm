S = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum = 0

A.sort()
B.sort(reverse=True)


for idx, val in enumerate(A):
    sum += val*B[idx]
 
print(sum)