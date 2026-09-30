def yell(text: str) -> str:
    """
    >>> yell("Hello!")
    'Hello!!'
    >>> yell("Really?")
    'Really??'
    >>> yell("Cringe? CRINGE!")
    'Cringe?? CRINGE!!'
    >>> yell("No punctuation")
    'No punctuation'
    >>> yell("First line! Second line?")
    'First line!! Second line??'
    """
    result = ""
    for character in text:
        result += character
        if character == "!" or character == "?":
            result += character
    return result


if __name__ == "__main__":
    text = input()
    print(yell(text))
