
class RGB:
    """
    >>> c = RGB(100, 150, 200)
    >>> print(c)
    RGB(100, 150, 200)
    >>> print(c.lighter(0.2))
    RGB(131, 171, 211)
    >>> print(c.darker(0.3))
    RGB(70, 105, 140)
    >>> print(c.invert())
    RGB(155, 105, 55)
    >>> print(c.to_hex())
    #6496c8
    >>> print(c)
    RGB(100, 150, 200)
    """

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def lighter(self, factor: float) -> 'RGB':
        red = round(self.red + (255 - self.red) * factor)
        green = round(self.green + (255 - self.green) * factor)
        blue = round(self.blue + (255 - self.blue) * factor)

        return RGB(red, green, blue)

    def darker(self, factor: float) -> 'RGB':
        red = round(self.red * (1 - factor))
        green = round(self.green * (1 - factor))
        blue = round(self.blue * (1 - factor))

        return RGB(red, green, blue)

    def invert(self) -> 'RGB':
        return RGB(
            255 - self.red,
            255 - self.green,
            255 - self.blue
        )

    def to_hex(self) -> str:
        red = hex(self.red)[2:].zfill(2)
        green = hex(self.green)[2:].zfill(2)
        blue = hex(self.blue)[2:].zfill(2)

        return f"#{red}{green}{blue}"

    def __str__(self) -> str:
        return f"RGB({self.red}, {self.green}, {self.blue})"


if __name__ == '__main__':
    c = RGB(100, 150, 200)
    print(c)

    print(c.lighter(0.2))
    print(c.darker(0.3))
    print(c.invert())
    print(c.to_hex())
