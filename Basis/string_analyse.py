def isspace(c: str) -> bool:
    """
    >>> isspace('hello world')
    True
    >>> isspace('hell')
    False
    """
    return ' ' in c or '\t' in c or '\n' in c

def isvowel(c: str) -> bool:
    """
    >>> isvowel('aaaa')
    True
    >>> isvowel('B')
    False
    """
    for char in c:
        if char not in "aeiou":
            return False
    return True

def has_single_vowel(s: str) -> bool:
    """
    >>> has_single_vowel('rhythm')
    False
    >>> has_single_vowel('apple' )
    False
    """
    aantal_klinkers = 0
    for char in s:
        if isvowel(char):
            aantal_klinkers += 1
    if aantal_klinkers == 1:
        return True
    else:
        return False


def count_vowels(s: str) -> int:
    """
    >>> count_vowels("Hello, world!")
    3
    >>> count_vowels("rhythm")
    0
    """
    aantal_klinkers = 0
    for char in s:
        if char in "aeiou":
            aantal_klinkers += 1
    return aantal_klinkers
