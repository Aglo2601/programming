import math


def is_priem(n: int) -> bool:
    """check for priemgetal"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def print_priemen_tot(N: int) -> None:
    """print priem nummers tot N"""
    for k in range(2, N):
        if is_priem(k):
            print(k)


def zoveelste_priem(N: int) -> int:
    """print het zoveelste priemgetal in reeks."""
    if N <= 0:
        raise ValueError("N moet een positief geheel getal zijn")
    count = 0
    cand = 2
    while True:
        if is_priem(cand):
            count += 1
            if count == N:
                return cand
        cand += 1


if __name__ == "__main__":
    while True:
        try:
            s = input("Naar het hoeveelste priemgetal bent u op zoek? ")
            n = int(s)
        except Exception:
            continue
        if n > 0:
            break
    print(zoveelste_priem(n))
