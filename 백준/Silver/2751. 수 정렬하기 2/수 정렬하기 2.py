import sys
input = sys.stdin.readline
N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))

numbers.sort()

for i in numbers:
    print(i)
