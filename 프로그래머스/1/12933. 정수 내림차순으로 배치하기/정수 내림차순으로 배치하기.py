def solution(n):
    nList = sorted(list(str(n)), reverse = True)
    return int("".join(nList))