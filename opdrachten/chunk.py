def chunk(values: list[int], n: int) -> list[list[int]]:
    """
    >>> chunk([1, 2, 3, 4, 5, 6], 2)
    [[1, 2], [3, 4], [5, 6]]
    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    >>> chunk([], 3)
    []
    """
    result = []
    current = []

    for value in values:
        current.append(value)
        if len(current) == n:
            result.append(current)
            current = []
    if current:
        result.append(current)
    return result