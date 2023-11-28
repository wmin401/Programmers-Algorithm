def solution(a, b):
    print(gcd(a, b))
    numerator = a/gcd(a, b)
    denominator = b/gcd(a, b)
    a_list = []
    
    while denominator % 2 == 0:
        denominator //= 2
    while denominator % 5 == 0:
        denominator //= 5
            
        
    if denominator == 1:
        return 1
    else:
        return 2
        


def gcd(a, b):
    if b > a:
        a, b = b, a
    while b:  
        a, b = b, a % b
        
    return  a