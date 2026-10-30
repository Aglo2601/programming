def merge_lists(lst1: list[int], lst2: list[int]) -> list[int]:
    """Merge two sorted lists of integers into a sorted list.

    >>> merge_lists([1, 2, 5], [4, 5, 6])
    [1, 2, 4, 5, 5, 6]
    >>> merge_lists([], [1, 3])
    [1, 3]
    >>> merge_lists([1, 2, 3], [])
    [1, 2, 3]
    >>> merge_lists([1, 2], [1, 2])
    [1, 1, 2, 2]
    >>> merge_lists([], [])
    []
    """
    result = []
    i = 0
    j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1

    if i < len(lst1):
        for value in lst1[i:]:
            result.append(value)
    elif j < len(lst2):
        for value in lst2[j:]:
            result.append(value)

    return result
