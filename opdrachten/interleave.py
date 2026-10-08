def interleave(first, second, keep=False):
    """

    >>> interleave([1, 2], ['a', 'b'])
    [1, 'a', 2, 'b']
    >>> interleave([1, 2, 3], ['a', 'b'], keep=True)
    [1, 'a', 2, 'b', 3]
    >>> interleave([1], ['a', 'b', 'c'], keep=False)
    [1, 'a']
    """
    result = []
    mean_length = min(len(first), len(second))

    for index in range(mean_length):
        result.append(first[index])
        result.append(second[index])

    if keep:
        result.extend(first[mean_length:])
        result.extend(second[mean_length:])

    return result