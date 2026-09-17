def reeks1() -> None:
	"""
	>>> reeks1()
	0
	2
	4
	6
	8
	10
	12
	14
	16
	18
	"""
	for i in range(10):
		print(i * 2)


def reeks2() -> None:
	"""
	>>> reeks2()
	1
	3
	5
	7
	9
	11
	13
	15
	17
	19
	21
	23
	"""
	for i in range(12):
		print(2 * i + 1)


def reeks3() -> None:
	"""
	>>> reeks3()
	1
	2
	5
	10
	17
	26
	37
	50
	65
	82
	101
	122
	145
	170
	197
	"""
	# start with 1 and keep adding successive odd numbers: 1,3,5,7,...
	value = 1
	add = 1
	for _ in range(15):
		print(value)
		value += add
		add += 2


def reeks4() -> None:
	"""
	>>> reeks4()
	5
	4
	3
	2
	1
	0
	-1
	-2
	-3
	"""
	for i in range(5, -4, -1):
		print(i)


def reeks5() -> None:
	"""
	>>> reeks5()
	1
	3
	9
	27
	81
	243
	729
	"""
	count = 0
	value = 1
	while count < 7:
		print(value)
		value *= 3
		count += 1


def reeks6() -> None:
	"""
	>>> reeks6()
	1000
	100
	10
	1
	0
	0
	0
	0
	0
	0
	"""
	count = 0
	value = 1000
	while count < 10:
		print(value)
		value = value // 10
		count += 1


def reeks7() -> None:
	"""
	>>> reeks7()
	1
	2
	*
	4
	5
	*
	7
	8
	*
	10
	"""
	for i in range(1, 11):
		if i % 3 == 0:
			print("*")
		else:
			print(i)


def reeks8() -> None:
	"""
	>>> reeks8()
	1
	2
	#
	8
	16
	#
	64
	128
	#
	512
	"""
	count = 0
	value = 1
	while count < 10:
		print(value)
		count += 1
		if count >= 10:
			break
		value *= 2
		print(value)
		count += 1
		if count >= 10:
			break
		print("#")
		count += 1
		if count >= 10:
			break
		value *= 4
