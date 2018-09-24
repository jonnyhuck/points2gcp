import csv

# set csv path
csv_path = "gcp_point_MR.points"

# init output string
out = ""

# open the file
with open(csv_path, "rb") as file:

	# read the file (binary mode)
	reader = csv.reader(file)
	
	# skip the header line
	next(reader, None)

	# for each line
	for row in reader:

		# convert to required format and append to output string
		out += "-gcp " + " ".join(row[:-1]) + " "

# print output string
print out