def solution(n, m):
 
    return [gcd(n, m), (n * m)//gcd(n, m)]

def gcd(n, m):
    if m > n:
        n, m = m, n
    
    while m > 0:
        n, m = m, n%m
    
    return n

