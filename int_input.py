def get_odd_number() -> int:
    """
    Deze functie vereist een oneven integer.
    """
    result = int(input("Enter an odd int: "))
    while result % 2 == 0:
        result = int(input("Enter an odd int: "))
    return result

def get_positive_int() -> int:
    getal = int(input("Geef een positief getal: "))
    while getal <= 0:
        getal = int(input("Geef een positief getal: "))
    return getal

def get_any_int_but_0() -> int:
    getal = int(input("Geef een geheel getal (niet 0): "))
    while getal == 0:
        getal = int(input("Geef een geheel getal (niet 0): "))
    return getal

def get_min_int(minimum: int) -> int:
    getal = int(input("Geef een geheel getal (minimaal {}): ".format(minimum)))
    while getal < minimum:
        getal = int(input("Geef een geheel getal (minimaal {}): ".format(minimum)))
    return getal

def get_two_different_ints() -> tuple[int, int]:
    int1 = int(input("Geef het eerste gehele getal: "))
    int2 = int(input("Geef het tweede gehele getal: "))
    while int1 == int2:
        print("De twee getallen moeten verschillend zijn.")
        int1 = int(input("Geef het eerste gehele getal: "))
        int2 = int(input("Geef het tweede gehele getal: "))
    return int1, int2

if __name__ == '__main__':
    get_positive_int()
    get_any_int_but_0()
    get_min_int(100)
    get_two_different_ints()