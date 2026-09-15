def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
    """
    >>> calculate_cafeine(1, 0, 0, 0)
    90
    >>> calculate_cafeine(2, 0, 0, 0)
    180
    >>> calculate_cafeine(0, 0, 0, 1)
    40
    >>> calculate_cafeine(0, 1, 0, 0)
    45
    """
    coffee = coffee * 90
    tea = tea * 45
    energy = energy * 80
    cola = cola * 40
    return coffee + tea + energy + cola

if __name__ == '__main__':
    coffee = int(input("hoeveel koffie heb je gedronken? "))
    tea = int(input("Hoeveel thee heb je gedronken? "))
    energy = int(input("hoeveel energie heb je gedronken? "))
    cola = int(input("Hoeveel cola heb je gedronken? "))
    result = calculate_cafeine(coffee, tea, energy, cola)
    print(f"Je krijgt {result} mg cafeïne binnen")
