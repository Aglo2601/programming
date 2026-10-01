def autocorrect(s: str) -> str:
    """
    >>> autocorrect('---')
    '-'
    >>> autocorrect('Dit hier,, dit kan niet de bedoeling   zijn.')
    'Dit hier, dit kan niet de bedoeling zijn.'
    """
    result = ''
    for char in s:
        if char.isalnum() or result.endswith(char):
            result += char
    return result
