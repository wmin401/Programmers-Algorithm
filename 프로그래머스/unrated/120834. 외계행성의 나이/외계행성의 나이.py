def solution(age):
    alphabat = 'abcdefghijklmnopqrstuvwxyz'
    
    answer = ''
    for i in str(age):
        answer += alphabat[int(i)]
    return answer