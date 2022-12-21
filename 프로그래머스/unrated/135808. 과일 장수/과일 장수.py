def solution(k, m, score):
    num_box = int(len(score)/m)
    answer = 0
    
    score.sort(reverse = True)
    
    for i in range(0,num_box):
        answer = answer + score[i*m+(m-1)]*m      
    

    return answer
