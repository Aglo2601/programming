def chunk(values, n):
    """
    >>> chunk([1, 2, 3, 4, 5, 6], 2)
    [[1, 2], [3, 4], [5, 6]]
    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    >>> chunk([], 3)
    []
    """
    result == []
    for index in range(0, len(values), n):
        result.append(values[index:index + n])
    return result
