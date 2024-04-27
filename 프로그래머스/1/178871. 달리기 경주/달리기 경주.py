def solution(players, callings):
    
    ranking = { player: idx for idx, player in enumerate(players)}
    
    for player in callings:
        idx = ranking[player]
        ranking[player] -= 1
        ranking[players[idx-1]] += 1
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        
    return players