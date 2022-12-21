def solution(k, tangerine):
    sum = 0
    answer = 0
    for index, num in enumerate(get_counts(tangerine)):
        sum += num
        if sum >= k:
            return index + 1
            

def get_counts(seq): 
    counts = {}
    for x in seq:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    
    return sorted(counts.values(), reverse=True)