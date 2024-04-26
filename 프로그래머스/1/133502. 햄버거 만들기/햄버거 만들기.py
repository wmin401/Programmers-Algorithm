def solution(ingredient):
    make = []
    cnt = 0
    
    for i in ingredient:
        make.append(i)
        if make[-4:] == [1,2,3,1]:
            cnt +=1
            for _ in range(4):
                make.pop()

    return cnt