def is_priem(getal):
	if getal < 2:
		return False
	if getal == 2:
		return True
	if getal % 2 == 0:
		return False

	for deler in range(3, int(getal ** 0.5) + 1, 2):
		if getal % deler == 0:
			return False

	return True


def print_priemen_tot(N):
	for getal in range(N):
		if is_priem(getal):
			print(getal)


def zoveelste_priem(N):
	gevonden = 0
	getal = 1

	while gevonden < N:
		getal += 1
		if is_priem(getal):
			gevonden += 1

	return getal


while True:
	try:
		N = int(input("Welk priemgetal (volgnummer) zoek je? "))
		break
	except ValueError:
		print("Voer een geheel getal in.")

print(zoveelste_priem(N))

