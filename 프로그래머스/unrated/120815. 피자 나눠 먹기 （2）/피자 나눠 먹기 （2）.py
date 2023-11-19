def solution(n):
    
    return lcm(n, 6) // 6

def gcd(a, b):
    if b > a :
        a, b = b, a
    
    while b:
        a, b = b, a%b
    
    return a

def lcm(a, b):
    return a*b//gcd(a, b)