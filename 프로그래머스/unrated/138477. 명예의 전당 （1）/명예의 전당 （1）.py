def solution(k, scores):
    answer = []
    temp = []
    for index, score in enumerate(scores):
        temp.sort()
        
        if k > index:
            temp.append(score)
            temp.sort()
        else:
            if(temp[0] < score):
                temp.pop(0)
                temp.append(score)                
            temp.sort()
        
        answer.append(temp[0])
        
    return answer