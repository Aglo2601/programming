def list_check_all_even(lst: list[int]) -> bool:
    """
    >>> list_check_all_even([2, 4, 0, -6])
    True
    >>> list_check_all_even([2, 3, 4])
    False
    >>> list_check_all_even([])
    True
    """
    for number in lst:
        if number % 2 != 0:
            return False
    return True


def list_count_even(lst: list[int]) -> int:
    """
    >>> list_count_even([1, 2, 3, 4, 6])
    3
    >>> list_count_even([-2, -1, 0, 5])
    2
    >>> list_count_even([])
    0
    """
    count = 0
    for number in lst:
        if number % 2 == 0:
            count += 1
    return count


def list_get_even(lst: list[int]) -> list[int]:
    """
    >>> list_get_even([1, 2, 3, 4, 6])
    [2, 4, 6]
    >>> list_get_even([-3, -2, 0, 5])
    [-2, 0]
    >>> list_get_even([])
    []
    """
    even_numbers = []
    for number in lst:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
