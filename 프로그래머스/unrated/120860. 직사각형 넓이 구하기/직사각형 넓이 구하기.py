def solution(dots):
    
    x_axis = [i[0] for i in dots]
    y_axis = [i[1] for i in dots]
    
    width = max(x_axis) - min(x_axis)
    height = max(y_axis) - min(y_axis)
    return width * height 