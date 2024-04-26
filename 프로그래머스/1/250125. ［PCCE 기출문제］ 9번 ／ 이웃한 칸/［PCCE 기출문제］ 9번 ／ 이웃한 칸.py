def solution(board, h, w):
    answer = 0
    color = board[h][w]
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    for i in range(len(dx)):
        h_check = h + dx[i]
        w_check = w + dy[i]
        if 0 <= h_check < len(board) and 0 <= w_check < len(board[0]):
            if color == board[h_check][w_check]:
                answer +=1
    return answer