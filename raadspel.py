import random

def check_guess(guess: int, number: int) -> bool:
    """
    Check of de gok goed is. Als de gok niet goed is, return dan
    False en print of de gok te groot of te klein is.

    >>> check_guess(5, 7)
    Je gok is te klein!
    False
    >>> check_guess(10, 3)
    Je gok is te groot!
    False
    >>> check_guess(4, 4)
    Je hebt het getal goed geraden, gefeliciteerd!
    True
    """
    if guess == number:
        print("Je hebt het getal goed geraden, gefeliciteerd!")
        return True
    if guess > number:
        print("Je gok is te groot!")
    else:
        print("Je gok is te klein!")
    return False

def decide_number(level: int) -> int:
    """
    Kies een willekeurig getal tussen 1 en level.

    >>> decide_number(1)
    1
    >>> decide_number(100) <= 100
    True
    >>> 1 <= decide_number(2) <= 2
    True
    """
    return random.randint(1, level)

if __name__ == '__main__':
    while True:
        s = input("Level: ").strip()
        if not s.isdigit():
            continue
        level = int(s)
        if level > 0:
            break

    number = decide_number(level)

    # loop gok tot decide_number geraden is
    while True:
        s = input("Gok: ").strip()
        if not s.isdigit():
            continue
        guess = int(s)
        if guess < 1 or guess > level:
            continue
        if check_guess(guess, number):
            break

