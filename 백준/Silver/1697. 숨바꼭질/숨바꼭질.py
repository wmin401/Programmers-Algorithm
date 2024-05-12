import sys
input = sys.stdin.readline

def bfs():
    queue = []
    queue.append(N)

    while queue:
        tmp = queue.pop(0)
        if tmp == K:
            print(dist[tmp])
            break
        for nx in (tmp - 1, tmp + 1, tmp * 2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[tmp] + 1
                queue.append(nx)



N, K = map(int, input().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1)
bfs()