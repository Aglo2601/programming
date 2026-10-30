def list_duplicates(numbers: list[int]) -> set[int]:
	"""Return the integers that occur at least twice.

	>>> list_duplicates([1, 2, 1, 3, 2, 2])
	{1, 2}
	>>> list_duplicates([4, 5, 6])
	set()
	>>> list_duplicates([])
	set()
	"""
	seen = set()
	duplicates = set()
	for number in numbers:
		if number in seen:
			duplicates.add(number)
		else:
			seen.add(number)
	return duplicates


def mating_pairs(
	females: set[object], males: set[object]
) -> set[tuple[object, object]]:
	"""Pair one female and one male at a time, consuming both input sets.

	>>> result = mating_pairs({'f1', 'f2'}, {'m1', 'm2'})
	>>> result in (
	...     {('f1', 'm1'), ('f2', 'm2')},
	...     {('f1', 'm2'), ('f2', 'm1')},
	...     {('m1', 'f1'), ('m2', 'f2')},
	...     {('m2', 'f1'), ('m1', 'f2')},
	... )
	True
	"""
	pairs: set[tuple[object, object]] = set()
	while females and males:
		pairs.add((females.pop(), males.pop()))
	return pairs


def count_values(data: dict[object, object]) -> int:
	"""Return the number of unique values in a dictionary."""
	return len(set(data.values()))


def minst_voorkomende(observations: dict[str, int]) -> str:
	"""Return the species name with the fewest observations."""
	return min(observations, key=observations.get)


def tel_dubbele(data: dict[object, object]) -> int:
	"""Return the number of distinct values occurring at least twice."""
	counts: dict[object, int] = {}
	for value in data.values():
		counts[value] = counts.get(value, 0) + 1
	return sum(count >= 2 for count in counts.values())


def is_normal(vector: dict[object, float]) -> bool:
	"""Return whether the dictionary's values sum to exactly 1.0."""
	return sum(vector.values()) == 1.0


def dict_intersect(
	first: dict[object, object], second: dict[object, object]
) -> dict[object, object]:
	"""Return key-value pairs that are identical in both dictionaries."""
	return {key: value for key, value in first.items() if second.get(key) == value and key in second}


def get_valuable_letters(minimum: int) -> int:
	"""Return how many Scrabble letters are worth at least ``minimum`` points."""
	scrabble_points = {
		'a': 1, 'b': 3, 'c': 5, 'd': 2, 'e': 1, 'f': 4, 'g': 3, 'h': 4,
		'i': 2, 'j': 4, 'k': 3, 'l': 3, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
		'q': 10, 'r': 2, 's': 2, 't': 2, 'u': 4, 'v': 4, 'w': 5, 'x': 8,
		'y': 8, 'z': 4,
	}
	return sum(points >= minimum for points in scrabble_points.values())


def emmeren(lists: list[list[int]]) -> dict[int, list[list[int]]]:
	"""Group lists by their length."""
	buckets: dict[int, list[list[int]]] = {}
	for values in lists:
		buckets.setdefault(len(values), []).append(values)
	return buckets
