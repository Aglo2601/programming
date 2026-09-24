def is_different(s1: str, s2: str) -> bool:
    """
    >>> is_different("abc", "abc")
    False
    >>> is_different("abc", "abd")
    True
    >>> is_different("abc", "abcd")
    True
    """
    if len(s1) > len(s2):
        lengte = len(s2)
    else:
        lengte = len(s1)

    for i in range(lengte):
        if s1[i] != s2[i]:
            return True

    if len(s1) != len(s2):
        return True

    return False


def count_difference(s1: str, s2: str) -> int:
    """
    >>> count_difference("abc", "abc")
    0
    >>> count_difference("abc", "abd")
    1
    >>> count_difference("abc", "def")
    3
    >>> count_difference("abc", "abcd")
    1
    """
    if len(s1) > len(s2):
        lengte = len(s2)
    else:
        lengte = len(s1)

    verschil = abs(len(s1) - len(s2))

    for i in range(lengte):
        if s1[i] != s2[i]:
            verschil += 1

    return verschil