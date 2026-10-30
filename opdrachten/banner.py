def longest_word_from_list(words: list[str]) -> str:
    """Geeft de langste string uit de lijst
    >>> longest_word_from_list(["Margherita", "Tutta", "la", "Vita"])
    'Margherita'
    >>> longest_word_from_list(["zon", "maan", "ster"])
    'maan'
    >>> longest_word_from_list(["", "a", "bb"])
    'bb'
    >>> longest_word_from_list(["gelijk", "lengte"])
    'gelijk'
    """
    longest_word = words[0]
    for word in words[1:]:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def print_banner(words: list[str]) -> None:
    """Print de woorden tussen twee regels hekjes.
    >>> print_banner(["Margherita", "Tutta", "la", "Vita"])
    ##########
    Margherita
    Tutta
    la
    Vita
    ##########
    >>> print_banner(["kat"])
    ###
    kat
    ###
    """
    border = "#" * len(longest_word_from_list(words))
    print(border)
    for word in words:
        print(word)
    print(border)

def string_to_list(message: str) -> list[str]:
    """Splits een string met woorden per spatie
    >>> string_to_list("Margherita Tutta la Vita")
    ['Margherita', 'Tutta', 'la', 'Vita']
    >>> string_to_list("hallo")
    ['hallo']
    >>> string_to_list("een twee drie")
    ['een', 'twee', 'drie']
    """
    words = []
    current_word = ""
    for character in message:
        if character == " ":
            words.append(current_word)
            current_word = ""
        else:
            current_word += character
    words.append(current_word)
    return words

if __name__ == "__main__":
    message = input("Typ een boodschap: ")
    words = string_to_list(message)
    print_banner(words)
	
