import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(list(set(numbers)))

dics = {sorted_numbers[i] : i for i in range(len(sorted_numbers))}

for key in numbers:
    print(dics[key], end =" ")