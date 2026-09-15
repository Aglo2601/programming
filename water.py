def hoeveelheid_water(minuten: int) -> int:
    """
    Geeft de hoeveelheid water uit de douche, gerekend in flesjes,
    gegeven het aantal minuten douchen.
    >>> hoeveelheid_water(0)
    0
    >>> hoeveelheid_water(10)
    120
    >>> hoeveelheid_water(137)
    1644
    """
    return minuten * 12

if __name__ == '__main__':
    # <vraag input, roep functie aan, en print resultaat
    minuten = int(input("hoeveel minuten douche jij? "))
    resultaat =  minuten * 12
    print(resultaat)
