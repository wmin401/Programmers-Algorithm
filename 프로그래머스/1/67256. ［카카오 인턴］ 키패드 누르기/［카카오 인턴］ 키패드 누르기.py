def solution(numbers, hand):
    
    number_dic = {1:(0,0), 2:(0,1), 3:(0,2),
                  4:(1,0), 5:(1,1), 6:(1,2),
                  7:(2,0), 8:(2,1), 9:(2,2),
                  "*":(3,0), 0:(3,1), "#":(3,2)}
    
    lhand = number_dic["*"]
    rhand = number_dic["#"]
    
    
    answer = ''
    
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            lhand = number_dic[i]
            
        elif i in [3,6,9]:
            answer += 'R'
            rhand = number_dic[i]
            
        elif i in [2,5,8,0]:
            if abs(number_dic[i][0] - lhand[0]) + abs(number_dic[i][1] - lhand[1]) < abs(number_dic[i][0] - rhand[0]) + abs(number_dic[i][1] - rhand[1]):
                answer += 'L'
                lhand = number_dic[i]
            elif abs(number_dic[i][0] - lhand[0]) + abs(number_dic[i][1] - lhand[1]) > abs(number_dic[i][0] - rhand[0]) + abs(number_dic[i][1] - rhand[1]):
                answer += 'R'
                rhand = number_dic[i]
            
            else: 
                if hand == 'right':
                    answer += 'R'
                    rhand = number_dic[i]
                else:
                    answer += 'L'
                    lhand = number_dic[i]
                    
    return answer