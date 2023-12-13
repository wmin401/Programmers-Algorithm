def solution(t, p):
    
    p_length = len(p)
    t_list = []
    p_list = []
    
    for i in range(len(t)):
        if (i + p_length) <= len(t):
            t_list.append(t[i:i + p_length])

    
    for num in t_list:
        if int(num) <= int(p):
            p_list.append(num)

    
            

    return len(p_list)