def solution(quiz):
    answer = []
    
    for equation in quiz:
        e_list = equation.split()
        result = int(e_list[0])
        operator = e_list[1]
        operand = e_list[2]
        
        if operator == "+":
            result += int(operand)
        else:
            result -= int(operand)
        
        if str(result) == e_list[4]:
            answer.append("O")
        elif str(result) != e_list[4]:
            answer.append("X")
            
            
    return answer