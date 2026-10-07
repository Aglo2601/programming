def uniq(lijst: list[object]) -> list[object]:
    """
    >>> uniq([])
    []
    >>> uniq([7])
    [7]
    >>> uniq([1, 2, 3])
    [1, 2, 3]
    >>> uniq([1, 1, 2, 1, 3, 2])
    [1, 2, 3]
    >>> uniq(['appel', 'peer', 'appel', 'banaan', 'peer'])
    ['appel', 'peer', 'banaan']
    >>> uniq([3, 1, 2, 1, 3])
    [3, 1, 2]
    >>> uniq([[1], [2], [1]])
    [[1], [2]]

    >>> invoer = [1, 2, 1]
    >>> resultaat = uniq(invoer)
    >>> invoer
    [1, 2, 1]
    >>> resultaat
    [1, 2]
    >>> resultaat is invoer
    False
    """
    resultaat = []
    for positie in range(len(lijst)):
        element = lijst[positie]
        if element not in resultaat:
            resultaat.append(element)
    return resultaat
