import sys

nums = list(map(int,sys.stdin.readline().split()))

r_nums = []

for i in nums:
  reverse = str(i)[::-1]
  r_nums.append(int(reverse))

if r_nums[0] > r_nums[1]:
  print(r_nums[0])
else:
  print(r_nums[1])