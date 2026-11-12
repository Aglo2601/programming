import sys, string

Index = dict[str, list[int]]


def read_stopwords() -> set[str]:
    """
    Read all the stopwords from the file "stopwords.txt". Returns the
    collection of stopwords as a set; each stopword should be stripped
    of whitespace.
    """
    stopwords = set()

    with open('stopwords.txt') as file:
        for word in file:
            word = convert_word(word)

            if word != "":
                stopwords.add(word)

    return stopwords


def convert_word(word: str) -> str:
    """
    Strips a word from all puncuation, whitespace, and digits. Then
    converts the word into all lower case.
    Don't worry about any other strange characters that are left
    in the text.

    >>> convert_word("Hello!")
    'hello'
    >>> convert_word("123Python456")
    'python'
    >>> convert_word("...WORLD...")
    'world'
    """
    return word.strip(string.punctuation +
                      string.whitespace +
                      string.digits).lower()


def create_index(filename: str, stopwords: set[str]) -> Index:
    """
    Reads `filename` and returns an index.
    * For each word in the file, the index contains a record of all line
      numbers where this word occurs.
    * Words are converted to lowercase and stripped of punctuation,
      whitespace and digits before adding to the index.
    * Empty strings and stopwords are ignored and not indexed.
    """

    book_index: Index = {}

    with open(filename, "r") as file:
        for line_number, line in enumerate(file, 1):
            word = ""

            for char in line:
                if char in string.whitespace:
                    word = convert_word(word)

                    if word != "" and word not in stopwords:
                        if word in book_index:
                            if line_number not in book_index[word]:
                                book_index[word].append(line_number)
                        else:
                            book_index[word] = [line_number]

                    word = ""
                else:
                    word += char

            word = convert_word(word)

            if word != "" and word not in stopwords:
                if word in book_index:
                    if line_number not in book_index[word]:
                        book_index[word].append(line_number)
                else:
                    book_index[word] = [line_number]

    return book_index


def search_index(word: str, book_index: Index) -> list[int]:
    """
    Find the word in book_index. Returns a list of the line numbers where
    word occurs. If the word does not occur, returns an empty list.

    >>> search_index("dinner", {"dinner": [258, 289]})
    [258, 289]
    >>> search_index("guest", {"dinner": [258, 289]})
    []
    >>> search_index("guest", {"guest": [1, 2]})
    [1, 2]
    """
    word = convert_word(word)

    if word in book_index:
        return book_index[word]

    return []


def show_search_results(
    searched_word: str, line_numbers: list[int]
) -> None:
    """
    Displays the search results (line_numbers) nicely, like in the
    examples.

    >>> show_search_results("dinner", [549, 1542])
    The word "dinner" can be found on lines: 549, 1542.
    >>> show_search_results("guest", [])
    The word "guest" was not found.
    >>> show_search_results("table", [10])
    The word "table" can be found on lines: 10.
    """
    if len(line_numbers) == 0:
        print(f'The word "{searched_word}" was not found.')
    else:
        print(
            f'The word "{searched_word}" can be found on lines: ',
            end=""
        )

        for i in range(len(line_numbers)):
            if i > 0:
                print(", ", end="")

            print(line_numbers[i], end="")

        print(".")


def user_input_search(book_index: Index) -> None:
    """
    User input loop. For every line provided as input, convert it,
    find the line numbers, and show results.
    """
    line = input("\nEnter search term: ")

    while line not in ["q", "Q", "quit", ""]:
        searched_word = convert_word(line)
        line_numbers = search_index(searched_word, book_index)
        show_search_results(searched_word, line_numbers)
        line = input("\nEnter search term: ")


if __name__ == "__main__":

    stopwords = read_stopwords()

    if len(sys.argv) < 2:
        print("No arguments provided.",
              "Please specifiy the file you want to search.")
        sys.exit()

    book_index = create_index(sys.argv[1], stopwords)

    print("Index built for", sys.argv[1]+".",
          "Type the word you want to look up.")

    user_input_search(book_index)
