def solution(board):
    n = len(board)
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    
    bomb = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bomb.append((i,j))
                
    for x, y in bomb:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                cnt += 1
        
   
    return cnt