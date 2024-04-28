def solution(answers):
    answer = [0,0,0]
    output = []
    
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    for idx in range(len(answers)):
        if answers[idx] == p1[idx % len(p1)]:
            answer[0] += 1
        if answers[idx] == p2[idx % len(p2)]:
            answer[1] += 1
        if answers[idx] == p3[idx % len(p3)]:
            answer[2] += 1
    
    for idx, i in enumerate(answer):
        if i == max(answer):
            output.append(idx+1)
            
    return output