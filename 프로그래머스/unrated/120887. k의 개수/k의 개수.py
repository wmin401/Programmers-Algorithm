def solution(i, j, k):

            
    return sum(str(n).count(str(k)) for n in range(i, j + 1) if str(k) in str(n))