import sys

nums = []

for i in range(10):
  nums.append(int(input())%42)

new_list = list(set(nums))

print(len(new_list))