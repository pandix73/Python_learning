def checkio(game_result):
    
    for i in range(0, 3):
        if game_result[i][0] != '.' and game_result[i][0] == game_result[i][1] and game_result[i][0] == game_result[i][2]:
            return game_result[i][0]
        elif game_result[0][i] != '.' and game_result[0][i] == game_result[1][i] and game_result[0][i] == game_result[2][i]:
            return game_result[0][i]
    if game_result[0][0] != '.' and game_result[0][0]== game_result[1][1] and game_result[2][2] == game_result[1][1]:
        return game_result[0][0]
    if game_result[2][0] != '.' and game_result[2][0]== game_result[1][1] and game_result[0][2] == game_result[1][1]:
        return game_result[2][0]
    return 'D'
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

