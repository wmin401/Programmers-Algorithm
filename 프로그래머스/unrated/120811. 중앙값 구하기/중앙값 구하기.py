def solution(array):
    
    aList = sorted(array)
    median_index = len(aList)//2
  
    answer = aList[median_index]
    return answer