N = int(input())
subjects = list(map(int, input().split()))

max_sub = max(subjects)
for i in range(N):
    subjects[i] = subjects[i] / max_sub * 100

avg_sub = sum(subjects) / len(subjects)
print(avg_sub)
