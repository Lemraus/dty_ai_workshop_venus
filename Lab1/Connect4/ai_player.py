from player import Player
from copy import deepcopy
import time

class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to"""

    def __init__(self):
        self.name = "Venus"

    def getColumn(self, board):
        timestamp_start = time.time()

        alpha = -1e6
        best_ai_i_score = [None, -1e6]

        for i in board.getPossibleColumns():  # i is the position of our pin
            board_turn1 = deepcopy(board)
            board_turn1.play(1, i)
            min_score = 1e6

            for j in board_turn1.getPossibleColumns():
                board_turn2 = deepcopy(board_turn1)
                board_turn2.play(-1, j)
                score = AIPlayer.score(board_turn2)
                if score < min_score:
                    min_score = score
                if score < alpha:
                    break

            if min_score > best_ai_i_score[1]:
                best_ai_i_score = [i, min_score]

        print(
            "Temps pris pour effectuer les calculs : ",
            time.time() - timestamp_start,
        )
        return best_ai_i_score[0]
    
    def ai_step(self, board, depth):
        pass

    @staticmethod
    def score(board):
        # base
        score_board = [
            [3, 4, 5, 7, 5, 4, 3],
            [4, 6, 8, 10, 8, 6, 4],
            [5, 8, 11, 13, 11, 8, 5],
            [5, 8, 11, 13, 11, 8, 5],
            [4, 6, 8, 10, 8, 6, 4],
            [3, 4, 5, 7, 5, 4, 3],
        ]
        S = 0
        for i in range(6):
            for j in range(7):
                S += score_board[i][j] * board[i][j]
        # alignements
        return S

    @staticmethod
    def explore_lignes(board):
        for j in range(6):
            if board[]
            allie_streak = 0
            adv_streak = 0
            for i in range(1, 7):
                pass

