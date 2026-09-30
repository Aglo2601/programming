def autocorrect(s: str) -> str:
    """
    >>> autocorrect('---')
    '-'
    >>> autocorrect('Dit hier,, dit kan niet de bedoeling   zijn.')
    'Dit hier, dit kan niet de bedoeling zijn.'
    """
    result = ''
    for char in s:
        if char.isalnum():
            result += char
        elif not result.endswith(char):
            result += char
    return result