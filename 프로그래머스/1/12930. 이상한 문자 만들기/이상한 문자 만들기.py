def solution(s):
    
    s_list = s.split(" ")
    answer = []
    
    
    for word in s_list:
        word_list = list(word)
        result = ''
        for i in range(len(word_list)):
            if i % 2 == 0:
                word_list[i] = word_list[i].upper()
            else:
                word_list[i] = word_list[i].lower()
        result = ''.join(word_list)
        answer.append(result)
    


    return " ".join(answer)