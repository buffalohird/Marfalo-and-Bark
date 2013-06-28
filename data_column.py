import csv, itertools, sys

ret_file = "tally-results.csv"
 
file_to_search = "data.csv"
	
ret_contents = []

search_field = ""
column_found = 0
chosen_column = 0
column_dictionary = {}

arg_length = len(sys.argv)
if(arg_length == 1):
	print "nothing"
else:
	if(arg_length == 2):
		search_field = sys.argv[1]

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
					if column == search_field:
						column_found = 1
						chosen_column = initial_counter
					initial_counter += 1
				counter += 1
			elif column_found == 1:
				result = row[chosen_column]
				if result in column_dictionary:
					column_dictionary[result] += 1
				else:
					column_dictionary[result] = 1
			else:
				print 

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

#print column_dictionary
final_list = []
for key, value in sorted(column_dictionary.iteritems(), key=lambda (k,v): (v,k)):
    final_list.append("%s: %s" % (key, value))
final_list.reverse()
print final_list
