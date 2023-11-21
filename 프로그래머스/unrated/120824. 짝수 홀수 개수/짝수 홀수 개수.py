def solution(num_list):
    
    even = [i for i in num_list if i % 2 == 0]
    

    return [len(even), len(num_list) - len(even)]