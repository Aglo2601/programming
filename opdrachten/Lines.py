
class Point:
    """
    >>> p1 = Point(1, 1)
    >>> print(p1.x)
    1
    >>> print(p1.y)
    1
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class LineSegment:
    """
    >>> segment = LineSegment(Point(1, 1), Point(3, 2))
    >>> segment.slope()
    0.5
    >>> segment.length()
    2.23606797749979
    >>> segment = LineSegment(Point(0, 0), Point(3, 4))
    >>> segment.slope()
    1.3333333333333333
    >>> segment.length()
    5.0
    """

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def slope(self) -> float:
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)

    def length(self) -> float:
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y

        return float((dx ** 2 + dy ** 2) ** (1 / 2))


if __name__ == '__main__':

    segment = LineSegment(Point(1, 1), Point(3, 2))
    print(segment.slope())  # <- 0.5
    print(segment.length()) # <- 2.23606797749979
