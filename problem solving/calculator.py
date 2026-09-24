def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.

    >>> evaluate(1, "+", 1)
    2.0
    >>> evaluate(100, "-", 9)
    91.0
    >>> evaluate(4, "*", -6)
    -24.0
    >>> evaluate(3, "/", 8)
    0.375
    """
    if y == "+":
        return float(x + z)
    elif y == "-":
        return float(x - z)
    elif y == "*":
        return float(x * z)
    else:
        return float(x / z)


if __name__ == '__main__':
    x, y, z = input().split()
    print(evaluate(int(x), y, int(z)))
