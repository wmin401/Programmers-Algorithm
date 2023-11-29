def solution(dots):
    
    x1, y1 = dots[0][0], dots[0][1]
    x2, y2 = dots[1][0], dots[1][1]
    x3, y3 = dots[2][0], dots[2][1]
    x4, y4 = dots[3][0], dots[3][1]
    
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    p4 = (x4, y4)
    
    # AB == CD
    if gradient(p1, p2) == gradient(p3, p4):
        return 1
    # AC == BD
    if gradient(p1, p3) == gradient(p2, p4):
        return 1
    # AD == BC
    if gradient(p1, p4) == gradient(p2, p3):
        return 1
    return 0

def gradient(a, b):
    
    if (a[0] - b[0]) != 0:
        return (a[1] - b[1]) / (a[0] - b[0])
    else:
        return 0