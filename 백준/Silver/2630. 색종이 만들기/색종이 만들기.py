import sys
input = sys.stdin.readline

def divide_conquer(x, y, N):
    global blue, white
    color = paper[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                divide_conquer(x, y, N//2)
                divide_conquer(x, y+N//2, N//2)
                divide_conquer(x+N//2, y, N//2)
                divide_conquer(x+N//2, y+N//2, N//2)
                return
    if color == 1:
        blue += 1
    else:
        white += 1


N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

blue, white = 0, 0
divide_conquer(0, 0, N)

print(white)
print(blue)













