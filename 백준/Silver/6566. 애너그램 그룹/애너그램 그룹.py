import collections

anagrams = collections.defaultdict(list)
li = []
tmp = []

while True:
    try:
        word = input()
        li.append(word)
    except EOFError:
        break

# asdk, kasd, asdkasdk, asdkaskd
# {'adks': ['asdk', 'kasd'], 'aaddkkss': ['asdkasdk', 'asdkaskd']}
for i in li:
    anagrams["".join(sorted(i))].append(i)

max_len = -1
for i in anagrams.keys():
    max_len = max(max_len, len(anagrams[i]))
    sorted_anagram = sorted(anagrams[i])
    tmp.append(sorted_anagram)

tmp.sort(key=lambda x: (max_len-len(x), x[0]))

range_ = 5
if range_ > len(tmp):
    range_ = len(tmp)

# 반복 제거 : list -> set -> list
for i in range(range_):
    print(f'Group of size {len(tmp[i])}: {" ".join(elem for elem in sorted(list(set(tmp[i]))))} .')