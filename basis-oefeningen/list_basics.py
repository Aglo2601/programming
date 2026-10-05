def list_contains_element(lst: list[object], elt: object) -> bool:
    """Return whether ``elt`` occurs in ``lst``, using a loop."""
    for element in lst:
        if element == elt:
            return True
    return False


def list_contains_no_element(lst: list[object], elt: object) -> bool:
    """Return whether ``elt`` does not occur in ``lst``, using a loop."""
    found = False
    for element in lst:
        if element == elt:
            found = True
            break
    return not found


def list_count_element(lst: list[object], elt: object) -> int:
    """Count occurrences of ``elt`` in ``lst``."""
    count = 0
    for element in lst:
        if element == elt:
            count += 1
    return count


def list_count_elements(lst: list[object], lst_elt: list[object]) -> int:
    """Count elements in ``lst`` matching any element in ``lst_elt``."""
    count = 0
    for element in lst:
        if element in lst_elt:
            count += 1
    return count
