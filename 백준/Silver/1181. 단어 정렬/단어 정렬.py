N = int(input())
word_list = []
for _ in range(N):
    word_list.append(input())

word_list = sorted(sorted(set(word_list)), key = lambda x: len(x))


for word in word_list:
    print(word)