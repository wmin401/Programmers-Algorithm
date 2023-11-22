def solution(emergency):
    sorted_emergency = sorted(emergency, reverse = True)
    answer = []
    for i in emergency:
        answer.append(sorted_emergency.index(i) + 1)
    return answer