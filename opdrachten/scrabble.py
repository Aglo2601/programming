



Alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

POINTS = [1, 3, 3,  2, 1, 4, 2, 4, 1, 8, 5, 1,  3,
          1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

def compute_score(word: str) -> int:
    """
    Bereken en return de score voor het woord.

    >>> compute_score("Hello")
    8
    >>> compute_score("abc!")
    7
    """
    total_score = 0
    for letter in word.upper():
        total_score += compute_letter_score(letter)
    return total_score

def compute_letter_score(letter: str) -> int:
    """
    Bereken en return de score voor één enkele letter.

    >>> compute_letter_score("Q")
    10
    >>> compute_letter_score("?")
    0
    """
    for index, character in enumerate("abcdefghijklmnopqrstuvwxyz"):
        if letter.lower() == character:
            return POINTS[index]
    return 0

if __name__ == '__main__':


    speler1 = input("Speler 1: ")
    score1 = compute_score(speler1)

    speler2 = input("Speler 2: ")
    score2 = compute_score(speler2)

    if score1 > score2:
        print("Speler 1 wint!")
    elif score2 > score1:
        print("Speler 2 wint!")
    else:
        print("Gelijkspel!")