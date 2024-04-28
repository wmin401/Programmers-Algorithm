def solution(arr):
    
    array_list = [arr[0]]

    
    
    for i in range(1, len(arr)):
        if arr[i] != array_list[-1]:
            array_list.append(arr[i])
            
    
     
    return array_list