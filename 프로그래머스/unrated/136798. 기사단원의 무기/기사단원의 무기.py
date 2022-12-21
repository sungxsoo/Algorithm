def solution(number, limit, power):
    answer = 0
    power_array = [0] * (number + 1)
    for i in range(1, number+1):
        count = 0
        for j in  range(i,number+1,i):
            power_array[j] +=1
                
    for i in power_array:
        if i > limit:
            answer += power
        else:
            answer += i
    
    return answer