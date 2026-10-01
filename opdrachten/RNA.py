def check_input(dna: str) -> bool:
	"""
	>>> check_input("ATGC")
	True
	>>> check_input("atGc")
	True
	>>> check_input("hello")
	False
	>>> check_input("")
	True
	"""
	for nucleotide in dna.upper():
		if nucleotide not in "ATGC":
			return False
	return True


def transcribe_dna_to_rna(dna: str) -> str:
	"""Schrijft DNA-elementen om naar RNA-elementen als hoofdletters.

	Ga ervan uit dat een valide string wordt gegeven.

	>>> transcribe_dna_to_rna("ATGC")
	'UACG'
	>>> transcribe_dna_to_rna("atGcAgtAttGCA")
	'UACGUCAUAACGU'
	"""
	rna = ""
	for nucleotide in dna.upper():
		if nucleotide == "A":
			rna += "U"
		elif nucleotide == "T":
			rna += "A"
		elif nucleotide == "G":
			rna += "C"
		elif nucleotide == "C":
			rna += "G"
	return rna


if __name__ == '__main__':
	dna = input("DNA: ")
	if check_input(dna):
		print(f"RNA: {transcribe_dna_to_rna(dna)}")
	else:
		print("That is not a valid DNA string")
