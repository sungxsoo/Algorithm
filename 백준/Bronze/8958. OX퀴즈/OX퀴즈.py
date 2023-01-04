T = int(input())
quiz_results = []

for i in range(T):
  quiz_results.append(input())

total_point = 0
bonus_point = 0

for result in quiz_results:
  for single_result in result:
    if single_result == 'O':
      total_point += 1
      total_point += bonus_point
      bonus_point += 1
    else:
      bonus_point = 0
      
  print(total_point)
  total_point = 0
  bonus_point = 0

      

