from itertools import combinations

def solution(nums):
    answer = 0
    nums_list = list(map(sum,combinations(nums, 3)))
    print(nums_list)
    
    for i in nums_list:
        count = 0
        for j in range(1,i+1):
            if i%j == 0:
                count += 1
        if count == 2:
            answer += 1

    return answer