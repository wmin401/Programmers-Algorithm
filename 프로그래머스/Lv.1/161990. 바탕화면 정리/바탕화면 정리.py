def solution(wallpaper):
    answer = [51, 51, 0, 0]
    lux, luy, rdx, rdy = 0, 1, 2, 3
    
    for i, elements in enumerate(wallpaper):
        for j, element in enumerate(elements):
            if element == '#':
                answer[lux] = min(answer[lux], i)
                answer[luy] = min(answer[luy], j)
                answer[rdx] = max(answer[rdx], i+1)
                answer[rdy] = max(answer[rdy], j+1)
                
    return answer