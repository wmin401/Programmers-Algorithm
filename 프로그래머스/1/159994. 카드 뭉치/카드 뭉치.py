def solution(cards1, cards2, goal):
    answer = []
            
    i = j = 0
    for word in goal:
        if i < len(cards1) and word == cards1[i]:
            answer.append(word)
            i += 1
        if j < len(cards2) and word == cards2[j]:
            answer.append(word)
            j += 1
    print("answer: ", answer)
    print("goal: ", goal)
    return "No" if answer != goal else "Yes"