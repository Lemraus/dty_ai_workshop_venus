def score(board):
    score_board = [
        [3, 4, 5, 7, 5, 4, 3],
        [4, 6, 8, 10, 8, 6, 4],
        [5, 8, 11, 13, 11, 8, 5],
        [5, 8, 11, 13, 11, 8, 5],
        [4, 6, 8, 10, 8, 6, 4],
        [3, 4, 5, 7, 5, 4, 3],
    ]
    S = 0
    # on fait une pause, on a fini le niveau 2, on essaiera d'aller plus loin après
    # nous on a fait une fonction d'évaluation globale on sait pas ce que ça vaut faut juste ajouter pour les alignements mnt

    for i in range(7):
        for j in range(6):
            S += score_board[i][j] * board[i][j]

    

    return S
