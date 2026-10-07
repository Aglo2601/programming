def contig(getallen):
	"""
	>>> contig([1, 2, 3, 6, 7, 9])
	[[1, 2, 3], [6, 7], [9]]
	>>> contig([4, 5, 2, 3, 4, 8])
	[[4, 5], [2, 3, 4], [8]]
	>>> contig([-3, -2, -1, 1, 0])
	[[-3, -2, -1], [1], [0]]
	"""
	if not getallen:
		return []

	groepen = [[getallen[0]]]
	for getal in getallen[1:]:
		if getal == groepen[-1][-1] + 1:
			groepen[-1].append(getal)
		else:
			groepen.append([getal])
	return groepen
