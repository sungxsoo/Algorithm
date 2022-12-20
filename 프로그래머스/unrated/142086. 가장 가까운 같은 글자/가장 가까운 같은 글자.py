def solution(s):
    answer = []
    word = ''
    for index, alphabet in enumerate(s):
        if index == s.find(alphabet):
            answer.append(-1)
        else:
            answer.append(index - word.rfind(alphabet))
        word = word + alphabet
    return answer