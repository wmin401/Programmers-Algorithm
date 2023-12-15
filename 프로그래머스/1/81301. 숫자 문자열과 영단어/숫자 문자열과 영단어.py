def solution(s):
    
    convert = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for num in convert:
        if num in s:
            s = s.replace(num, str(convert.index(num)))
          
    

    return int(s)