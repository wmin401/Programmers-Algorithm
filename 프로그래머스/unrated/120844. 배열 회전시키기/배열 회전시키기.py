def solution(numbers, direction):
    answer = []
    if direction == "right":
        numbers.insert(0, numbers.pop())
    else:
        numbers.append(numbers[0])
        del numbers[0]
            
            
    return numbers