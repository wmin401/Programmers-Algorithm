import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graphs,v, visited):
    visited[v] = True
    
    for i in graphs[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(graphs, i, visited)


N, M  = map(int, input().split())
graphs = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

visited = [0] * (N + 1)
count = 0
for i in range(1,N+1):
    if visited[i] == False:
        dfs(graphs, i, visited)
        count +=1
        
print(count)
