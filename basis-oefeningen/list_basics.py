def list_contains_element(lst: list[object], elt: object) -> bool:
    """
    >>> list_contains_element([1, 2, 3], 2)
    True
    >>> list_contains_element([1, 2, 3], 4)
    False
    """
    for element in lst:
        if element == elt:
            return True
    return False


def list_contains_no_element(lst: list[object], elt: object) -> bool:
    """
    >>> list_contains_no_element([1, 2, 3], 2)
    False
    >>> list_contains_no_element([1, 2, 3], 4)
    True
    """
    found = False
    for element in lst:
        if element == elt:
            found = True
            break
    return not found


def list_count_element(lst: list[object], elt: object) -> int:
    """
    >>> list_count_element([1, 2, 2, 3], 2)
    2
    >>> list_count_element([1, 2, 3], 4)
    0
    """
    count = 0
    for element in lst:
        if element == elt:
            count += 1
    return count


def list_count_elements(lst: list[object], lst_elt: list[object]) -> int:
    """
    >>> list_count_elements([1, 2, 2, 3], [2, 4])
    2
    >>> list_count_elements([1, 2, 3], [4, 5])
    0
    """
    count = 0
    for element in lst:
        if element in lst_elt:
            count += 1
    return count
