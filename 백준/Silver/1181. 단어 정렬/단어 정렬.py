N = int(input())

words = []

for i in range(N):
  words.append(input())

words = sorted(list(set(words)))
words.sort(key=len)

for word in words:
  print(word)