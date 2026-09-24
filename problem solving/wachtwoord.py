def check_length(password: str) -> bool:
    """
    Controleer of het wachtwoord minstens 8 karakters bevat.

    >>> check_length("Aardappel")
    True
    >>> check_length("hoi")
    False
    """
    return len(password) >= 8

def check_letter(password: str) -> bool:
    """
    Controleer of het wachtwoord zowel een grote als een
    kleine letter bevat.
    Gebruik een loop om door password te lopen.

    >>> check_letter("Aardappel")
    True
    >>> check_letter("aardappel")
    False
    """
    has_upper = False
    has_lower = False

    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True

    return has_upper and has_lower

def check_number(password: str) -> bool:
    """
    Controleer of het wachtwoord een cijfer bevat.
    Gebruik een loop om door password te lopen.

    >>> check_number("wachtwoord1")
    True
    >>> check_number("wachtwoord")
    False
    """
    for character in password:
        if character.isdigit():
            return True

    return False

def check_password(password: str) -> bool:
    """
    Controleer of aan alledrie de eisen is voldaan.

    >>> check_password("Aardappel123")
    True
    >>> check_password("hoi")
    False
    """
    return check_length(password) and check_letter(password) and check_number(password)


if __name__ == '__main__':
     # <Hoofdprogramma mag maar één functie aanroepen>
    password = input("Geef een wachtwoord: ")
    if check_password(password):
        print("Het gegeven wachtwoord is valide.")
    else:
        print("Het gegeven wachtwoord is niet valide.")
