def solution(id_pw, db):
    answer = ''
    
    if id_pw in db:
        return "login"
    for info in db:
        
        if id_pw[0] == info[0] and id_pw[1] != info[1]:
            return 'wrong pw'
        
    return 'fail'
    