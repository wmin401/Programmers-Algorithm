K, N = map(int, input().split())
line = []
for _ in range(K):
    number = int(input())
    line.append(number)

start, end = 1, max(line)


while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in line:
        cnt += i // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)