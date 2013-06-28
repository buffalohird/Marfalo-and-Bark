import csv, itertools

ret_file = "search-results.csv"

print "\n\n\n\nHey, looking for all the rows in a .csv or .xls file (excel) that contain a specific set of characters?"
print """Follow the instructions here and we'll do what we can. 
Hopefully, this program is saved in the same folder as the spreadsheet you're trying to search and
you have saved the file as a .csv instead of a .xls.

The rows will be searched and the rows containing the characters you're looking for will be 
saved in a .csv file called """ + ret_file + """ in the same folder. Note that if you have a file
called """ + ret_file + """ in the folder already, it will be overwritten if you continue. 
(press control-C, not command-C, at any time to quit program) \n \n"""
 
file_to_search = raw_input("What file are you trying to search? (Case-sensitive, include the extension .csv) \n")

search_exps = []
add_more_queries = 'yes'

while add_more_queries != 'no':
	search_exps.append(raw_input("Type in an exact set of characters you are searching for: (i.e. .ma or 45@hall) \n"))
	add_more_queries = raw_input("Add more search expressions? (type in yes or no) \n")
	print '\n\n'
	


ret_contents = []

print "\nTrying to open file\n"

try:
	# open file in "universal new-line mode" so that it handles empty excel cells better
	with open(file_to_search, 'rU') as csvfile:
		csv_reader = csv.reader(csvfile)
		for row in csv_reader:
			added = False
			for cell in row:
				if added == False:
					for exp in search_exps:
						if exp in cell and added == False:
							ret_contents.append(row)
							added = True
							print "expression found in cell: " + cell

		if (ret_contents == []):
			print '\nExpression not found in file\n'
except IOError:
	print "IOERROR is raised. Are you sure you are in the right folder? We couldn't find the file you gave us.\n\n"
	exit(1)

print '\nTrying to write new file to ' + ret_file + '\n'

with open(ret_file, 'w+') as writefile:
	csv_writer = csv.writer(writefile)
	for row in ret_contents:
			csv_writer.writerow(row)

print 'Results should all be written in ' + ret_file
