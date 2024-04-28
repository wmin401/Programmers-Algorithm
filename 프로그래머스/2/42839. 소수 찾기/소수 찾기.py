from itertools import permutations

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False 
    
    return True

def solution(numbers):
    number_list = list(numbers)
    answer = 0
    all_numbers = set()
    
    for i in range(1, len(number_list) + 1):
        perm = permutations(number_list, i)
        for p in perm:
            all_numbers.add(int(''.join(p)))
    
    for num in all_numbers:
        if isPrime(num):
            answer += 1

    
    return answer