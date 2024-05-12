import sys
input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))


meetings.sort(key = lambda x: (x[1], x[0]))
cnt, end = 0, 0
for s, e in meetings:
    if s >= end:
        cnt +=1
        end = e

print(cnt)