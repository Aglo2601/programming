def check_answer(answer: str) -> bool:
    """
    Controleer of het antwoord op de vraag één van de opties
    42, tweeenveertig, of tweeënveertig is.
    >>> check_answer("42")
    True
    >>> check_answer("tweeenveertig")
    True
    >>> check_answer("tweeënveertig")
    True
    """
    return answer in ["42", "tweeenveertig", "tweeënveertig"]

if __name__ == '__main__':
    answer = input("De grote vraag van het leven, het universum en alles daarbij? ")
    if check_answer(answer):
        print("Ja")
    else:
        print("Nee") 