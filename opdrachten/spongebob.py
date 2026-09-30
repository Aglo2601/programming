def spongebob1(s: str) -> str:
    """
    >>> spongebob1('hello world!')
    'hElLo wOrLd!'
    >>> spongebob1('')
    ''
    >>> spongebob1('abc 123')
    'aBc 123'
    """
    result = ''
    for i in range(len(s)):
        if i % 2 == 1:
            result += s[i].upper()
        else:
            result += s[i]
    return result


def spongebob2(s: str) -> str:
    """
    >>> spongebob2('hello world!')
    'hElLo WoRlD!'
    >>> spongebob2('')
    ''
    >>> spongebob2('abc 123')
    'aBc 123'
    """
    result = ''
    letter_count = 0
    for char in s:
        if char.isalpha():
            letter_count += 1
            if letter_count % 2 == 1:
                char = char.lower()
            else:
                char = char.upper()
        result += char
    return result

