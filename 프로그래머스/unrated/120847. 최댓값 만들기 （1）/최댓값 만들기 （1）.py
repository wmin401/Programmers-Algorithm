def solution(numbers):
    
    answer = [max(numbers)]
    numbers.remove(max(numbers))
    answer.append(max(numbers))
    return answer[0] * answer[1]