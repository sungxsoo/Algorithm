number = 1
for i in range(3):
  number *= int(input())

numbers = ['0','1','2','3','4','5','6','7','8','9']

count = 0
counter = []

for num in numbers:
  for n in str(number):
    if num == n:
      count += 1
  counter.append(count)
  count = 0
  
for count in counter:
  print(count)