def solution(array, commands):
    answer = []
    
    
    for idx in commands:
        array_list = array[idx[0] - 1: idx[1]]
        array_list.sort()
        
        print(array_list)
        
        
        answer.append(array_list[idx[2] - 1])
         


        
    return answer