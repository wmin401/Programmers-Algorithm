def solution(brown, yellow):
    candinate = []
    answer = []
    
    
    dimension = brown + yellow
    
    for i in range(1, dimension + 1):
        if dimension % i == 0 and i >= dimension//i:
            candinate.append([i, dimension//i])
        
    for num in candinate:
        if 2*num[0] + 2*num[1] - 4 == brown:
            return num
            
    
        
 