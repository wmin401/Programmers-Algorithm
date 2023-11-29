def solution(polynomial):
    xnum = 0
    const = 0
    
    for element in polynomial.split(' + '):
        if element.isdigit():
            const += int(element)
        else:
            xnum = xnum + 1 if element == 'x' else xnum + int(element[:-1])
    if xnum == 0:
        return str(const)
    elif xnum == 1:
        return 'x + ' + str(const) if const != 0 else 'x'
    else:
        return f'{xnum}x + {const}' if const != 0 else f'{xnum}x'
  