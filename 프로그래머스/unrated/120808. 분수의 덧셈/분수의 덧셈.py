def gcd(d1, d2):
    if d2 > d1:
        d1, d2 = d2, d1    
    while d2:
        d1, d2 = d2, d1%d2
    return d1

def solution(numer1, denom1, numer2, denom2):
   
    num = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    common = gcd(num, denom)
    
    
    return [num//common, denom//common]