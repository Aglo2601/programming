def stretch(s: str) -> str:
    """
    >>> stretch('abc')
    'abbccc'
    >>> stretch('Hoi!')
    'Hooiii!!!!'
    """
    woord = ''
    teller = 1
    for char in s:
        woord += char * teller
        teller += 1
    return woord
