import math

N = str(input())

numbers = ['0','1','2','3','4','5','6',
          '7','8','9']

count = 0
num_count = []
six_or_nine = 0

for index,num in enumerate(numbers):
  for n in N:  
    if num == n:
      count += 1
  if num == '6' or num =='9':
    six_or_nine += count
    count = 0
    continue
  num_count.append(count)
  count = 0
num_count.append(math.ceil(six_or_nine / 2))

print(max(num_count))