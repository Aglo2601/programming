def remove_vowels(text: str) -> str:
    """
    >>> remove_vowels("just setting up my twitter")
    'jst sttng p my twttr'
    >>> remove_vowels("twiiitiitr")
    'twttr'
    >>> remove_vowels("")
    ''
    """
    vowels = "aeiouAEIOU"
    result = ""
    for character in text:
        if character not in vowels:
            result += character
    return result


if __name__ == "__main__":
    word = input()
    print(remove_vowels(word))

