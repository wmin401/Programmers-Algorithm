def solution(keyinput, board):
    answer = [0,0]
    
    for direction in keyinput:
        
        if direction == 'left':
            answer[0] -= 1
            if answer[0] < (board[0] - 1)//-2:
                answer[0] = (board[0] -1)//-2
        elif direction == 'right':
            answer[0] += 1
            if answer[0] > board[0]//2:
                answer[0] = board[0]//2
        elif direction == "down":
            answer[1] -= 1
            if answer[1] < (board[1] - 1) //-2:
                answer[1] = (board[1] -1) //-2
        elif direction == "up":
            answer[1] += 1
            if answer[1] > board[1]//2:
                answer[1] = board[1]//2
        
            
    return answer