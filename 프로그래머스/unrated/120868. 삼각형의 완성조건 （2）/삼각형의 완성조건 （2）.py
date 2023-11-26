def solution(sides):

    return (max(sides) - (max(sides) + 1 - min(sides)) + 1)  + (sum(sides) - max(sides) - 1)