def solution(my_string):
    
    print(list(my_string))
    word_list = []
    for i in my_string:
        if i not in word_list:
            word_list.append(i)
    return ''.join(word_list)