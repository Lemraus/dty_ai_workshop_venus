from player import Player
from copy import deepcopy
import time
import traceback
import random
from board import Board


class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to"""

    def __init__(self):
        self.name = "Venus"
        self.max_depth = 2

    def getColumn(self, board):
        timestamp_start = time.time()

        alpha = -1e6
        best_col = None

        for col in board.getPossibleColumns():
            next_board = deepcopy(board)
            next_board.play(self.color, col)
            if self.score(deepcopy(next_board)) > 500:
                return col
            try:
                beta = self.max_step(next_board, 0, 1e6, alpha)
            except:
                traceback.print_exc()
            if beta > alpha:
                alpha = beta
                best_col = col

        print(
            "Temps pris pour effectuer les calculs : ", time.time() - timestamp_start,
        )
        return best_col

    def max_step(self, board, depth, min_beta, max_alpha):
        alpha = -1e6
        for col in board.getPossibleColumns():
            next_board = deepcopy(board)
            next_board.play(-self.color, col)
            next_board_score = self.score(deepcopy(next_board))
            if next_board_score > 500:
                return next_board_score
            if depth == self.max_depth:
                alpha_candidate = next_board_score
            else:
                alpha_candidate = self.min_step(
                    next_board, depth + 1, min_beta, max(alpha, max_alpha)
                )
            if alpha_candidate > min_beta:
                return alpha_candidate
            if alpha_candidate > alpha:
                alpha = alpha_candidate
        return alpha

    def min_step(self, board, depth, min_beta, max_alpha):
        beta = 1e6
        for col in board.getPossibleColumns():
            next_board = deepcopy(board)
            next_board.play(self.color, col)
            next_board_score = self.score(deepcopy(next_board))
            if next_board_score < -500:
                return next_board_score
            if depth == self.max_depth:
                beta_candidate = next_board_score
            else:
                beta_candidate = self.max_step(
                    next_board, depth + 1, min(beta, min_beta), max_alpha
                )

            if beta_candidate < max_alpha:
                return beta_candidate
            if beta_candidate < beta:
                beta = beta_candidate
        return beta

    def score(self, board):
        # base
        score_board = [
            [5, 8, 11, 13, 11, 8, 5],
            [5, 8, 11, 13, 11, 8, 5],
            [4, 6, 8, 10, 8, 6, 4],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
        S = 0

        for i in range(6):
            for j in range(7):
                S += score_board[i][j] * board.getRow(i)[j]
        # alignements
        S += self.xplore_Diag_up(board)
        S += self.xplore_columns_smart(board)

        return S

    def xplore_columns_smart(self, board, valeur=[0, 1, 5, 18, 1000, 0]):
        bonus_columns = 0

        for j in board.getPossibleColumns():

            # getting column without zeros
            col = board.getCol(j)
            while col and col[-1] == 0:
                col.pop()

            if col:  # Continue si la colonne est non vide
                top_pin = col.pop()
                streak = 1

                while col and top_pin == col.pop():
                    streak += 1
                # on ajoute la valeur
                bonus_columns += top_pin * valeur[streak]

        return self.color * bonus_columns

    def xplore_Diag_up(self, board, bonus=[0, 1, 5, 18, 1000]):

        diag_bonus = 0
        for i in range(-5, 7):
            liste = board.getDiagonal(True, i)

            allie_streak = 0
            adv_streak = 0
            for j in liste:  # incrémentation des streaks aliés et adv
                if j == self.color:
                    allie_streak += 1
                    adv_streak = 0
                if j == -self.color:
                    adv_streak += 1
                    allie_streak = 0
            diag_bonus += (allie_streak * bonus[allie_streak]) - (
                adv_streak * bonus[adv_streak]
            )
            allie_streak = 0
            adv_streak = 0
        diag_down_bonus = self.xplore_Diag_down(board, sum_bonus=diag_bonus)
        return diag_bonus + diag_down_bonus

    def xplore_Diag_down(self, board, sum_bonus, bonus=[0, 1, 5, 18, 1000]):

        diag_bonus = 0
        for i in range(-5, 7):
            liste = board.getDiagonal(False, i)
            allie_streak = 0
            adv_streak = 0
            for j in liste:  # incrémentation des streaks aliés et adv
                if j == self.color:
                    allie_streak += 1
                    adv_streak = 0
                if j == -self.color:
                    adv_streak += 1
                    allie_streak = 0

            diag_bonus += (allie_streak * bonus[allie_streak]) - (
                adv_streak * bonus[adv_streak]
            )
        return diag_bonus

    def xplore_lines_smart(self, board, valeur=[0, 1, 5, 18, 200]):
        bonus_lines = 0
        for i in range(6):
            line = list(filter(lambda x: x != 0, board.getRow(i)))
            for streak in range(2, 5):
                # print(streak)
                for j in range(7 - streak):
                    k = sum(line[j : j + streak])
                    # print("   ", k)
                    if k >= streak:
                        bonus_lines += valeur[streak]
                    elif k <= -(streak):
                        bonus_lines -= valeur[streak]
        return self.color * bonus_lines
