def solution(A, B):
    cnt1 = 0

    
    while A != B:
        A = A[-1] + A[0:-1]
        cnt1 += 1
        if cnt1 > len(A):
            return -1
  
    return cnt1
