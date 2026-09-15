from prime.priem_getal import is_priem


def zoek_langste_reeks(N: int):
    """Find the longest run of consecutive non-prime numbers below N.

    Return (onder, boven) where both bounds are non-prime and onder <= boven.
    """
    prev_prime = None
    best_len = 0
    best_onder = 0
    best_boven = 0

    k = 2
    while k < N:
        if is_priem(k):
            if prev_prime is None:
                prev_prime = k
            else:
                gap = k - prev_prime - 1
                if gap > best_len:
                    best_len = gap
                    best_onder = prev_prime + 1
                    best_boven = k - 1
                prev_prime = k
        k += 1

    return best_onder, best_boven


def print_boodschap(N: int, onder: int, boven: int) -> None:
    lengte = boven - onder + 1 if boven >= onder else 0
    print(f"De langste reeks niet-priemgetallen onder de {N} begint op {onder} en eindigt bij {boven}")
    print(f"De reeks is {lengte} lang.")


if __name__ == "__main__":
    onder, boven = zoek_langste_reeks(10000)
    print_boodschap(10000, onder, boven)
