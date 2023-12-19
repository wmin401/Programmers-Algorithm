def solution(a, b, n):
    answer = 0
    
    while n >= a:
        
        print(answer)
        answer += b * (n // a)
        n = (n % a) + (b * (n // a))  
       
        print("n: ", n)
        
    
    
        
    return answer