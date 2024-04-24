def solution(number, limit, power):
    answer = []
    
    for i in range(1, number + 1):
        cnt = []
        for j in range (1,  int(i**0.5) + 1):
            if i % j == 0:
               cnt.append(j)
               cnt.append(i//j)
                    
        answer.append(len(set(cnt)))
    
    total = 0
    for i in answer:
        if i > limit:
            total +=  power
        else:
            total += i
    return total