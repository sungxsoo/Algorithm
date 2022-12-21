def solution(foods):
    answer = '0'
    
    foods.reverse()
    
    for index,food in enumerate(foods):
        num = len(foods) - ( index + 1 ) 
        for i in range (0, int(food/2)):
            answer = str(num) + answer + str(num)

    return answer