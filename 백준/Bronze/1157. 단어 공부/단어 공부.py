words =  str(input()).upper()

# 중복 제거
unq_words = list(set(words))

word_compator = []
word_counter = []

for w in unq_words:
  count = words.count(w)
  word_counter.append(count)

if word_counter.count(max(word_counter)) > 1:
  print('?')
else: 
  index = word_counter.index(max(word_counter))
  print(unq_words[index])
    