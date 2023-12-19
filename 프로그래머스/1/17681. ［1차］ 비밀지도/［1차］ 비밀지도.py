def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        
        merged_row = bin(arr1[i] | arr2[i])[2:]
        
        merged_row = '0' * (n - len(merged_row)) + merged_row
        
        
        answer.append(''.join("#" if num == '1' else " " for num in merged_row))
    
    
    
    
    

                
        
    return answer