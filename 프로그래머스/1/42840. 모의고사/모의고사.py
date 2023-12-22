def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    result = [0, 0, 0]
    output = []
    
    for idx, answer in enumerate(answers):
        
        if answer == p1[idx%len(p1)]:
            result[0] += 1
        if answer == p2[idx%len(p2)]:
            result[1] += 1
        if answer == p3[idx%len(p3)]:
            result[2] += 1
            
    if result[0] == max(result):
        output.append(1)
    if result[1] == max(result):
        output.append(2)
    if result[2] == max(result):
        output.append(3)
            
    return output