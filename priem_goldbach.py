from priem_getal import is_priem


def check_goldbach(upper: int = 1000) -> None:
    """Check Goldbach's conjecture for even numbers up to `upper` (inclusive).

    For each even number print a representation as sum of two primes, or
    report a failure if none is found.
    """
    for n in range(4, upper + 1, 2):
        found = False
        for a in range(2, n // 2 + 1):
            b = n - a
            if is_priem(a) and is_priem(b):
                print(f"{n} = {a} + {b}")
                found = True
                break
        if not found:
            print(f"Goldbach faalt voor {n}")
            return


if __name__ == "__main__":
    check_goldbach(1000)
