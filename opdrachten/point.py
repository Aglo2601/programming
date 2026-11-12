
class Point:
    """
    >>> p1 = Point(2, 3)
    >>> p2 = Point(5, -1)
    >>> print(p1)
    (2, 3)
    >>> print(p2)
    (5, -1)
    >>> p3 = p1 + p2
    >>> print(p3)
    (7, 2)
    >>> print(p1.distance_to(p2))
    5.0
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def distance_to(self, other: 'Point') -> float:
        dx = self.x - other.x
        dy = self.y - other.y

        return float((dx ** 2 + dy ** 2) ** (1 / 2))


if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point(5, -1)
    p3 = p1 + p2
    print(p3)

    print(p1.distance_to(p2))
