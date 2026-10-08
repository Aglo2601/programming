def uniq(lijst: list[object]) -> list[object]:
    """
    >>> uniq([2, 2, 2, 2])
    [2]
    >>> uniq([1, 1, 2, 1, 3, 2])
    [1, 2, 3]
    >>> uniq(["a", "b", "a"])
    ['a', 'b']
    """
    resultaat = []
    for positie in range(len(lijst)):
        check = lijst[positie]
        if check not in resultaat:
            resultaat.append(check)
    return resultaat
