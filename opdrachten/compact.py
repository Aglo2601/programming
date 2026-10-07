def compact(items: list[object]) -> list[object]:
    """
    >>> compact([0, 1, 2, 0, 3])
    [1, 2, 3]
    >>> compact(['', 'hello', '', 'world'])
    ['hello', 'world']
    >>> compact([False, True, None, 'yes'])
    [True, 'yes']
    >>> compact([[], [1], {}, {'a': 1}])
    [[1], {'a': 1}]
    >>> compact([])
    []
    >>> compact([0, '', False, None])
    []
    >>> values = [0, 'keep', '', 4]
    >>> result = compact(values)
    >>> result
    ['keep', 4]
    >>> values
    [0, 'keep', '', 4]
    >>> result is values
    False
    """
    result = []
    for item in items:
        if item:
            result.append(item)
    return result
