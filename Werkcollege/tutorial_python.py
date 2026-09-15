"""
tutorial_python.py

Kopieer elke functie uit de uitleg hiernaast naar dit bestand en vul daarna
de body in. Klik op de knop doctest om je werk te controleren.
"""

import math



def kwadraat(a: int) -> int:
    """
    >>> kwadraat(6)
    36
    >>> kwadraat(2)
    4
    """
    return a * a


def derde_macht(a: int) -> int:
    """
    >>> derde_macht(2)
    8
    >>> derde_macht(5)
    125
    """
    return a * a * a


def avg3(a: float, b: float, c: float) -> float:
    """
    >>> avg3(1, 2, 3)
    2.0
    >>> avg3(10, 20, 60)
    30.0
    """
    return (a + b + c)/3
    
    


def celsius_to_fahrenheit(c: float) -> float:
    """
    >>> celsius_to_fahrenheit(100)
    212.0
    >>> celsius_to_fahrenheit(0)
    32.0
    """
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    """
    >>> fahrenheit_to_celsius(212)
    100.0
    >>> fahrenheit_to_celsius(32)
    0.0
    """
    return (f - 32) * 5 / 9


def is_divisible(a: int, b: int) -> bool:
    """
    >>> is_divisible(10, 5)
    True
    >>> is_divisible(10, 3)
    False
    """
    return a % b == 0


def is_leap_year(y: int) -> bool:
    """
    >>> is_leap_year(2024)
    True
    >>> is_leap_year(2023)
    False
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
    True
    """
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0


def pythagoras(a: float, b: float) -> float:
    """
    >>> pythagoras(3, 4)
    5.0
    >>> pythagoras(5, 12)
    13.0
    """
    return math.sqrt(a * a + b * b)


def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """
    >>> is_valid_triangle(3, 4, 5)
    True
    >>> is_valid_triangle(1, 2, 10)
    False
    >>> is_valid_triangle(1, 1, 2)
    False
    """
    return a + b > c and b + c > a and a + c > b
    
    


def solve_quadratic(a: float, b: float, c: float) -> tuple:
    """
    >>> solve_quadratic(1, -3, 2)
    (2.0, 1.0)
    >>> solve_quadratic(1, 0, -4)
    (2.0, -2.0)
    """
    D = b * b - 4 * a * c
    return (-b + math.sqrt(D))/2*a, (-b - math.sqrt(D))/2*a


def count_leap_years(start: int, end: int) -> int:
    """
    >>> count_leap_years(2000, 2001)
    1
    >>> count_leap_years(2020, 2024)
    2
    >>> count_leap_years(1800, 1900)
    24
    """
    aantal = 0
    for y in range(start, end + 1):
        if is_leap_year(y):
            aantal = aantal + 1
    return  aantal


def nth_leap_year(start: int, n: int) -> int:
    """
    >>> nth_leap_year(2000, 1)
    2000
    >>> nth_leap_year(1800, 1)
    1804
    >>> nth_leap_year(2000, 3)
    2008
    """
    year = start
    count = 0
    while True:
        if is_leap_year(year):
            count += 1
            if count == n:
                break
        year += 1
    return year
