def shout(text: str) -> str:
    """
    >>> shout("Hello!")
    'HELLO!'
    >>> shout("Who the hell put the muffins the freezer?")
    'WHO THE HELL PUT THE MUFFINS THE FREEZER?'
    """
    result = ""
    for character in text:
        if character.isalpha():
            result += character.upper()
        else:
            result += character
    return result


if __name__ == "__main__":
    word = input()
    print(shout(word))

