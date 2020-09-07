import random
from board import Board


def boardalea(self):
    b = Board()
    ordre = random.randint(7, size=20)
    for i in range(len(ordre)):
        if ordre[i] in b.getPossibleColumns():
            b.play((i % 2)*2 - 1, ordre[i])

    print(ordre)
    print(b)
    return b


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
        diag_bonus += (allie_streak *
                       bonus[allie_streak]) - (adv_streak * bonus[adv_streak])
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

        diag_bonus += (allie_streak *
                       bonus[allie_streak]) - (adv_streak * bonus[adv_streak])
    return diag_bonus
