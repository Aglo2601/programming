def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    maaltijd ontbijt: 07:00 - 08:00
    maaltijd lunch: 12:00 - 13:00
    maaltijd avondeten: 18:00 - 19:00

    >>> meal("7:15")
    'ontbijt'
    >>> meal("08:00")
    'ontbijt'
    >>> meal("13:00")
    'lunch'
    >>> meal("18:53")
    'avondeten'
    >>> meal("22:12")
    """
    parts = time.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    total_minutes = hours * 60 + minutes
    if 7 * 60 <= total_minutes <= 8 * 60:
        return "ontbijt"
    if 12 * 60 <= total_minutes <= 13 * 60:
        return "lunch"
    if 18 * 60 <= total_minutes <= 19 * 60:
        return "avondeten"
    return None


if __name__ == "__main__":
    answer = meal(input("Hoe laat is het? "))
    if answer is not None:
        print(f"Het is tijd voor {answer}")
