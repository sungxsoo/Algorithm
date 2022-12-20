def solution(s):
    count = 0
    answer = 0
    letter = ''
    new = True
    
    for alphabet in s:
        if letter == '':
            answer += 1
            count += 1
            letter = alphabet 
        else:
            if letter == alphabet:
                count += 1
            else:
                count -= 1
        
        if count == 0:
            letter = ''
            
    return answer