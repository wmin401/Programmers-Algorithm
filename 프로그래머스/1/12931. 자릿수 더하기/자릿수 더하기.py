def solution(n):
    answer = 0
    nList = list(str(n))
    for i in range(len(nList)):
        answer += int(nList[i])

    return answer