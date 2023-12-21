def solution(nums):
    
    pocket = len(nums)//2
    pocket_list = []
    
    nums_set =  set(nums)
    if len(nums_set) >= pocket:
        return pocket
    else:
        return len(nums_set)
        
        
    