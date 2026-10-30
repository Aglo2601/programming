def selection_sort(l: list[int]) -> list[int]:
	"""Sorteert ``l`` in-place met het selection-sort-algoritme.

	>>> selection_sort([])
	[]
	>>> selection_sort([7])
	[7]
	>>> selection_sort([1, 2, 3, 4])
	[1, 2, 3, 4]
	>>> selection_sort([4, 3, 2, 1])
	[1, 2, 3, 4]
	>>> selection_sort([3, 1, 2])
	[1, 2, 3]
	>>> selection_sort([5, -2, 0, -8, 3])
	[-8, -2, 0, 3, 5]
	>>> selection_sort([2, 1, 2, 1, 0])
	[0, 1, 1, 2, 2]
	>>> waarden = [9, 4, 6, 2]
	>>> resultaat = selection_sort(waarden)
	>>> resultaat is waarden
	True
	>>> waarden
	[2, 4, 6, 9]
	"""
	for i in range(len(l)):
		kleinste_index = i
		for j in range(i + 1, len(l)):
			if l[j] < l[kleinste_index]:
				kleinste_index = j

		l[i], l[kleinste_index] = l[kleinste_index], l[i]

	return l

