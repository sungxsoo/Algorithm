T = int(input())

data = []
new_word = ''
new_word_list = []

for i in range(T):
  data.append(list(map(str, input().split())))



for d in data:
  for word in d[1]:
    for i in range(int(d[0])):
      new_word += word
  new_word_list.append(new_word)
  new_word = ''

for new_word in new_word_list:
  print(new_word)