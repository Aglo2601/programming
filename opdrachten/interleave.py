def interleave(lijst1: list[int], lijst2: list[int], keep: bool = False) -> list[int]:
    """
    >>> interleave([1, 2], [3, 4])
    [1, 3, 2, 4]
    >>> interleave([1, 2, 3], [4, 5], keep=True)
    [1, 4, 2, 5, 3]
    >>> interleave([1], [2, 3, 4], keep=False)
    [1, 2]
    """
    result: list[int] = []

    if len(lijst1) < len(lijst2):
        shorty = len(lijst1)
    else:
        shorty = len(lijst2)

    for index in range(shorty):
        result.append(lijst1[index])
        result.append(lijst2[index])

    if keep:
        for index in range(shorty, len(lijst1)):
            result.append(lijst1[index])
        for index in range(shorty, len(lijst2)):
            result.append(lijst2[index])

    return result