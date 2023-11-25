def solution(my_string, num1, num2):
    my_list = list(my_string)
    swap = my_list[num1]
    my_list[num1] = my_list[num2]
    my_list[num2] = swap
    return ''.join(my_list)