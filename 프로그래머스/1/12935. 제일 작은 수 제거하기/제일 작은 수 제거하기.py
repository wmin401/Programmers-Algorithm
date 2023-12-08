def solution(arr):
    
    arr_list = sorted(arr, reverse = True)
    
    arr.remove(arr_list[-1])
    
    if len(arr) > 0:
        return arr
    else:
        return [-1]

    