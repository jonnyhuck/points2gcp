import csv

# set csv path
csv_path = "pointsfile.points"

# init output string
out = ""

# open the file
with open(csv_path, "rt") as file:

	# read the file (text mode)
	reader = csv.reader(file)
	
	# skip the header line
	next(reader, None)

	# for each line
	for row in reader:

		# convert to required format and append to output string (-gcp pixel line easting northing elevation)
		out += "-gcp " + " ".join([ str(round(float(row[2]),3)), str(abs(round(float(row[3]),3))), row[0], row[1]]) + " "

# print output string
print(out)