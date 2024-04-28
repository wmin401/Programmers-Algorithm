def solution(citations):
    citations.sort(reverse = True)
    h_index = 0     
    for idx, citation in enumerate(citations):
        if citation >= idx + 1:
            h_index = idx + 1
    
    return h_index
    
   
