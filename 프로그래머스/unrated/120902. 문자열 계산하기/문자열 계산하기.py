def solution(my_string):
    my_list = my_string.split()
    answer = int(my_list[0])
    
    for i in range(1, len(my_list), 2):
        operator = my_list[i]
        operand =  int(my_list[i + 1])
        if operator == "+":
            answer += operand
        else:
            answer -= operand
    return answer