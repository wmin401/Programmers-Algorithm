def solution(x):
    x_list = list(str(x))
    x_list = [int(i) for i in x_list]
    
    if x % sum(x_list) == 0:
        return True
    return False