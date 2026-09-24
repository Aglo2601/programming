def calculate_grade(text: str) -> int:
    """
    >>> calculate_grade("One fish. Two fish. Red fish. Blue fish.")
    -9
    
    >>> calculate_grade("Congratulations! Today is your day. You're "
    ...     "off to Great Places! You're off and away!")
    3
    
    >>> calculate_grade("There are more things in Heaven and Earth, "
    ...     "Horatio, than are dreamt of in your philosophy.")
    9
    """ 

    letters = 0
    words = 0
    sentences = 0
    in_word = False

    for character in text:
        if character.isalpha():
            letters += 1

        if character in ".!?":
            sentences += 1

        if character.isspace():
            in_word = False
        elif not in_word:
            words += 1
            in_word = True

    return coleman_liau(words, sentences, letters)

def coleman_liau(words: int, sentences: int, letters: int) -> int:
    """
    Bereken de Coleman-Liau-index.
    """
    l = letters / words * 100
    s = sentences / words * 100

    cli = round(0.0588 * l - 0.296 * s - 15.8)
    return cli

if __name__ == '__main__':
    text = input('Text: ')
    grade = calculate_grade(text)

    if grade < 1:
        print('Below Grade 1')
    elif grade >= 16:
        print('Grade 16+')
    else:
        print(f'Grade {grade}')
    