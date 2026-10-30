def special_sort(l: list[int]) -> list[int]:
    """Sorteer ``l`` in-place en retourneer dezelfde lijst.

    >>> values = [3, 1, 2]
    >>> special_sort(values)
    [1, 2, 3]
    >>> values
    [1, 2, 3]
    >>> special_sort([])
    []
    >>> special_sort([1])
    [1]
    >>> special_sort([1, 2, 3])
    [1, 2, 3]
    >>> special_sort([3, 2, 1])
    [1, 2, 3]
    >>> special_sort([4, 1, 4, 2, 1])
    [1, 1, 2, 4, 4]
    """
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l
