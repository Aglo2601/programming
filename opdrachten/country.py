
class Country:
    """
    >>> canada = Country('Canada', 34482779, 9984670)
    >>> print(canada.name)
    Canada
    >>> print(canada.population)
    34482779
    >>> print(canada.area)
    9984670
    >>> usa = Country('United States of America', 313914040, 9826675)
    >>> print(canada.is_larger(usa))
    True
    >>> print(canada.population_density())
    3.4536
    >>> usa = Country('United States of America', 313914040, 9826675)
    >>> print(usa)
    United States of America has a population of 313914040 and is 9826675 square km.
    """

    def __init__(self, name: str, population: int, area: int):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other: 'Country') -> bool:
        return self.area > other.area
    
    def population_density(self) -> float:
        return round(self.population / self.area, 4)

    def __str__(self) -> str:
        return (f"{self.name} has a population of {self.population} "
                f"and is {self.area} square km.")


if __name__ == '__main__':

    # stap 1
    # per land: naam, aantal mensen, opp. in vierkante kilometers
    canada = Country('Canada', 34482779, 9984670)
    print(canada.name)
    print(canada.population)
    print(canada.area)

    # stap 2
    usa = Country('United States of America', 313914040, 9826675)
    print(canada.is_larger(usa))

    # stap 3
    # bevolkingsdichtheid <- mensen per vierkante kilometer
    print(canada.population_density())

    # stap 4
    # definieer de __str__ method
    usa = Country('United States of America', 313914040, 9826675)
    print(usa)
