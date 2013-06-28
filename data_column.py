import csv, itertools

ret_file = "tally-results.csv"
 
file_to_search = "data.csv"

search_exps = []

	
ret_contents = []

print "\nTrying to open file\n"

try:
	# open file in "universal new-line mode" so that it handles empty excel cells better
	with open(file_to_search, 'rU') as csvfile:
		csv_reader = csv.reader(csvfile)
		counter = 0
		for row in csv_reader:
			if counter == 0:
				initial_counter = 0
				for column in row:
					print column
					initial_counter += 1
				counter += 1
		if (ret_contents == []):
			print '\nNo data to Export\n'
except IOError:
	print "IOERROR is raised. Are you sure you are in the right folder? We couldn't find the file you gave us.\n\n"
	exit(1)

print '\nTrying to write new file to ' + ret_file + '\n'

with open(ret_file, 'w+') as writefile:
	csv_writer = csv.writer(writefile)
	for row in ret_contents:
			csv_writer.writerow(row)

print 'Results should all be written in ' + ret_file
