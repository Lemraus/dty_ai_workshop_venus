from player import Player
import numpy as np
import datetime


class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to"""

    def __init__(self):
        self.name = "Venus"

    def getColumn(self, board):
        timestamp_start = datetime.datetime.now()
        # TODO(student): implement this!
        # s = np.zeros((7, 7)) useful in min/max, useless in alpha/beta

        alpha, beta = -1000000, 1000000

        for i in board.getPossibleColumns():  # i is the position of our pin
            # on ajoute notre pin au board
            # board_turn1 = board + truc
            # if alpha_truc:

            #     continue
            board_turn1 = board
            board_turn1.play(None, i)

            for j in board_turn1.getPossibleColumns():
                # on ajoute le pin adverse au board
                # board_turn2 = board_turn1 + pin

                board_turn2 = board_turn1
                board_turn2.play(None, j)
                beta_candidate = AIPlayer.score(board_turn2)

                if beta_candidate < alpha:
                    break

        print(
            "Temps pris pour effectuer les calculs : ",
            datetime.datetime.now() - timestamp_start,
        )
        return best_play

    @staticmethod
    def score(board):
        pass
