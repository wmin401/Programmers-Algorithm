def solution(s):
    
    s_list = s.split(" ")
    stack = []
    for i in s_list:
        if i == "Z":
            stack.pop()
        else:
            stack.append(int(i)) 
        
    
    return sum(stack)