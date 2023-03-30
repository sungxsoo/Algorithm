import sys

num_list =  list(map(int, sys.stdin.readline().split()))

sum = 0

for i in num_list:
  sum += pow(i, 2)

print(sum % 10)