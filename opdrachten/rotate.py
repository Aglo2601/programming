def rotate(lst: list[object]) -> None:
    """

    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]
    >>> n2 = ['a', 'b']
    >>> rotate(n2)
    >>> n2
    ['b', 'a']
    >>> n3 = [42]
    >>> rotate(n3)
    >>> n3
    [42]
    >>> n4 = []
    >>> rotate(n4)
    >>> n4
    []
    """
    if not lst:
        return

    first = lst[0]
    for index in range(len(lst) - 1):
        lst[index] = lst[index + 1]
    lst[-1] = first
