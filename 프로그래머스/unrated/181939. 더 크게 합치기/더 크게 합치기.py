def solution(a, b):
    answer = 0
    
    a1 = int(str(a) + str(b))
    b1 = int(str(b) + str(a))
    
    if a1 > b1:
        answer = a1
    elif a1 < b1:
        answer = b1
        
    else:
        answer = a1
        
    return int(answer)