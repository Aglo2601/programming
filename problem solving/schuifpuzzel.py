
Board = list[list[int]]


def is_won(board: Board) -> bool:
    """
    Controleert of het bord in een winnende configuratie staat.
    Geeft True als
    de configuratie winnend is, False als dat niet het geval is.

    >>> is_won(
    ...     [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
    True
    >>> is_won(
    ...     [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 1, 2, 0]])
    False
    >>> is_won(
    ...     [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]])
    False
    """
    getal = 1

    for i in range(4):
        for j in range(4):
            if i == 3 and j == 3:
                if board[i][j] != 0:
                    return False
            else:
                if board[i][j] != getal:
                    return False
                getal += 1

    return True


def move_tile(board: Board, tile: int) -> bool:
    """
    Als de te verplaatsen tegel verplaatsbaar is:
    schuift de tegel in de
    configuratie van het bord en geeft True.
    Als dat niet het geval is,
    blijft het bord in de oorspronkelijke
      configuratie en functie geeft False.

    >>> board = [
    ...     [1, 2, 3, 4], [5, 6, 7, 8],
    ...     [9, 10, 11, 12], [13, 14, 0, 15]]
    >>> move_tile(board, 15)
    True
    >>> board
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    >>> move_tile(board, 1)
    False
    """
    tile_row = 0
    tile_col = 0
    empty_row = 0
    empty_col = 0

    for i in range(4):
        for j in range(4):
            if board[i][j] == tile:
                tile_row = i
                tile_col = j

            if board[i][j] == 0:
                empty_row = i
                empty_col = j

    if tile_row == empty_row:
        if tile_col + 1 == empty_col or tile_col - 1 == empty_col:
            board[empty_row][empty_col] = tile
            board[tile_row][tile_col] = 0
            return True

    if tile_col == empty_col:
        if tile_row + 1 == empty_row or tile_row - 1 == empty_row:
            board[empty_row][empty_col] = tile
            board[tile_row][tile_col] = 0
            return True

    return False


def print_board(board: Board) -> None:
    """
    Print alle rijen van het bord onder elkaar.
    Het format is zoals in de
    voorbeelden onderaan de opdracht.

    >>> print_board(
    ...     [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
     1  2  3  4
     5  6  7  8
     9 10 11 12
    13 14 15  0
    >>> print_board(
    ...     [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 1, 2, 0]])
    15 14 13 12
    11 10  9  8
     7  6  5  4
     3  1  2  0
    >>> print_board(
    ...     [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
     1  2  3  4
     5  6  7  8
     9 10 11 12
    13 14 15  0
    """
    for i in range(4):
        for j in range(4):
            if j == 3:
                print(f'{board[i][j]:2}')
            else:
                print(f'{board[i][j]:2}', end=' ')


def create_board() -> Board:
    """
    Initialiseert een bord van formaat 4 x 4.
    Sorteert de nummers op aflopende volgorde van
    inks boven naar rechts beneden.
    De volgorde van de tegels 1 en 2 is verwisseld.

    >>> create_board()
    [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 1, 2, 0]]
    >>> len(create_board())
    4
    >>> len(create_board()[0])
    4
    """
    board = [
        [15, 14, 13, 12],
        [11, 10, 9, 8],
        [7, 6, 5, 4],
        [3, 1, 2, 0]
    ]

    return board


if __name__ == '__main__':
    print("Welkom bij de schuifpuzzel!")
    board = create_board()
    while not is_won(board):
        print_board(board)
        tile = input("Tegel die je wil schuiven: ")
        valid = move_tile(board, int(tile))
        if not valid:
            print("Deze tegel kan je niet schuiven.")
    print("Gefeliciteerd, je hebt de schuifpuzzel opgelost!")
