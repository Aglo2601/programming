with open("inputfile.txt") as input_file, open("outputfile.txt", "w") as output_file:
	for line in input_file:
		output_file.write(line)
