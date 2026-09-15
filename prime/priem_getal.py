import math


def is_priem(n: int) -> bool:
    """Return True if n is a prime number, else False."""
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
    """Print all prime numbers strictly less than N, one per line."""
    for k in range(2, N):
        if is_priem(k):
            print(k)


def zoveelste_priem(N: int) -> int:
    """Return the N-th prime (1-based)."""
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
    # Vraag de gebruiker herhaaldelijk om een positieve rangorde
    while True:
        try:
            s = input("Naar het hoeveelste priemgetal bent u op zoek? ")
            n = int(s)
        except Exception:
            # Specification: we may assume an integer is entered, but be safe
            continue
        if n > 0:
            break
    print(zoveelste_priem(n))
