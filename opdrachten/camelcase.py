def convert(text: str) -> str:
    """
    >>> convert("check")
    'check'
    >>> convert("convertInput")
    'convert_input'
    >>> convert("readFromFile")
    'read_from_file'
    """
    result = ""
    for character in text:
        if character.isupper():
            result += "_" + character.lower()
        else:
            result += character
    return result


if __name__ == "__main__":
    camel_case = input("camelCase: ")
    print("snake_case:", convert(camel_case))