import sys
input = sys.stdin.readline
from collections import deque

def bfs(i, j ):
    queue = deque()
    queue.append((i,j))

    visited[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if maps[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))










n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

visited = [[-1] * m for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()