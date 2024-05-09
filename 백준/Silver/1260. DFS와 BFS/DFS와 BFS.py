def dfs(V):
    visited[V] = 1
    print(V, end = ' ')

    for i in graphs[V]:
        if visited[i] == 0:
            dfs(i)

def bfs(V):

    queue = []
    queue.append(V)
    visited[V] = 1
    while queue:
        tmp = queue.pop(0)
        print(tmp, end=" ")
        for i in graphs[tmp]:
            if visited[i] != 1:
                visited[i] = 1
                queue.append(i)


N, M, V = map(int, input().split())
graphs= [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

for i in graphs:
    i.sort()

visited = [0] * (N + 1)

dfs(V)
print()
visited = [0] * (N + 1)
bfs(V)



















