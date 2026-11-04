
import random


def calculate_points(board: list[int]) -> int:
    """
    Berekent het aantal punten dat is behaald met sjoelen. De
    volgorde van de punten is [2, 3, 4, 1]. Wanneer er een
    kwartet tussen zit, telt dit voor 20 punten.

    >>> calculate_points([3, 4, 3, 5])
    65
    >>> calculate_points([4, 3, 3, 5])
    64
    >>> calculate_points([0, 0, 0, 0])
    0
    >>> calculate_points([1, 1, 1, 1])
    20
    """
    punten = [2, 3, 4, 1]
    kwartetten = min(board)

    totaal = kwartetten * 20

    for i in range(4):
        totaal += (board[i] - kwartetten) * punten[i]

    return totaal


def shuffle_round(board: list[int], discs: int) -> int:
    """
    Simuleert een enkele ronde sjoelen. De variable `board` wordt
    aangepast als er een schijf in een gleuf terecht komt. Returnt
    het aantal schijven dat nog over is om nog eens mee te schuiven.

    >>> board = [0, 0, 0, 0]
    >>> over = shuffle_round(board, 0)
    >>> over
    0
    >>> sum(board)
    0
    >>> board = [0, 0, 0, 0]
    >>> over = shuffle_round(board, 30)
    >>> 0 <= over <= 30
    True
    >>> sum(board) + over == 30
    True
    """
    over = 0

    for i in range(discs):
        kans = random.uniform(0, 1)

        if kans <= 0.25:
            bak = random.uniform(0, 1)

            if bak <= 0.3:
                board[3] += 1
            elif bak <= 0.6:
                board[0] += 1
            elif bak <= 0.8:
                board[1] += 1
            else:
                board[2] += 1
        else:
            over += 1

    return over


if __name__ == '__main__':

    # <Zet het bord klaar, simuleer drie rondes en
    #  bereken aan het eind het aantal punten op basis van
    #  de staat van het sjoelbord>
    
    board = [0, 0, 0, 0]
    discs = 30

    for i in range(3):
        discs = shuffle_round(board, discs)

    print(f'Je bent geëindigd op deze configuratie: {board}')
    print(f'Dat zijn {calculate_points(board)} punten!')
