def convert_temperature(old_type: str, old_temp: int) -> int:
    """
    Zet de temperatuur (old_temp) van het type old_type om naar
    de temperatuur van het nieuwe type.

    De omrekening volgt de gegeven formules:
    - C -> F: F = (18C + 320) / 10
    - F -> C: C = (10F - 320) / 18

    Alle waarden worden afgerond op gehele graden volgens de voorbeelden in
    de opdracht: bij negatieve getallen wordt de waarde naar nul afgerond.

    >>> convert_temperature('C', 0)
    32
    >>> convert_temperature('F', 0)
    -17
    >>> convert_temperature('c', 20)
    68
    >>> convert_temperature('F', 10)
    -12
    """
    normalized_type = old_type.upper()

    if normalized_type == 'C':
        return int((18 * old_temp + 320) / 10)
    if normalized_type == 'F':
        return int((10 * old_temp - 320) / 18)

    raise ValueError(f"Ongeldige eenheid: {old_type}")


def print_table(old_type: str, begin_temp: int, end_temp: int, step_size: int) -> None:
    """
    Print de conversie-tabel.

    Als de eindtemperatuur niet groter is dan de begintemperatuur, wordt alleen
    de kopregel uitgeprint.

    >>> print_table('C', 0, 20, 5)
      C |   F
      0 |  32
      5 |  41
     10 |  50
     15 |  59
     20 |  68
    >>> print_table('F', 0, 10, 3)
      F |   C
      0 | -17
      3 | -16
      6 | -14
      9 | -12
    >>> print_table('F', 100, 0, 3)
      F |   C
    """
    normalized_type = old_type.upper()
    new_type = 'F' if normalized_type == 'C' else 'C'

    print(f"{normalized_type:>3} | {new_type:>3}")

    if end_temp <= begin_temp:
        return

    current_temp = begin_temp
    while current_temp <= end_temp:
        converted_temp = convert_temperature(normalized_type, current_temp)
        print(f"{current_temp:>3} | {converted_temp:>3}")
        current_temp += step_size


if __name__ == '__main__':
    while True:
        unit = input('Welke eenheid van temperatuur (C of F)? ').strip()
        if unit.upper() in {'C', 'F'}:
            unit = unit.upper()
            break

    begin_temp = int(input('Wat is de begintemperatuur? '))
    end_temp = int(input('Wat is de eindtemperatuur? '))

    while True:
        step_size = int(input('Wat is de stapgrootte? '))
        if step_size > 0:
            break

    print_table(unit, begin_temp, end_temp, step_size)
