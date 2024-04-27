def timeToConvert(today):
    year, month, day = map(int, today.split("."))
    return year * 12 * 28 + month * 28 + day


def solution(today, terms, privacies):
    answer = []
    todays = timeToConvert(today)
    
    terms_dic = {}
    for word in terms:
        term, period = word.split()
        terms_dic[term] = int(period) * 28
    
    for idx, word in enumerate(privacies):
        start, term = word.split()
        end = timeToConvert(start) + terms_dic[term]
        
        if end <= todays:
            answer.append(idx + 1)
    
    return answer