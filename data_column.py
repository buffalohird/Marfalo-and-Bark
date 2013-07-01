import csv, itertools, sys

#loads in and caches the spreadsheet
def load_data(chosen_file):

	new_cache = []
	try:
		# open file in "universal new-line mode" so that it handles empty excel cells better
		with open(chosen_file, 'rU') as csvfile:
			csv_reader = csv.reader(csvfile)
			counter = 0
			for row in csv_reader:
				counter += 1
				new_cache.append(row)
			return new_cache
	except IOError:
		print "IOERROR is raised. Are you sure you are in the right folder? We couldn't find the file you gave us.\n\n"
		exit(1)

#end load_data()

def filter_data(cached_data, column, argument):

	result_data = []
	try:
		row_counter = 0
		for row in cached_data:
			if row_counter == 0:
				result_data.append(row)
				row_counter += 1
			else:
				result = row[column]
				if result.lower() == argument.lower():
					result_data.append(row)
				row_counter += 1

		return result_data

	except IOError:
		print "IOERROR is raised. Are you sure you are in the right folder? We couldn't find the file you gave us.\n\n"
		exit(1)

#end filter_data(cached_data, column, argument)


def find_column(cached_data, filter_field):
	row_counter = 0.
	counter = 0
	for row in cached_data:
		if row_counter == 0:
			for field in row:
				if field.lower() == filter_field.lower():
					return counter
				counter += 1
			row_counter += 1
		else:
			return 0

#end find_column(cached_data, argument)

def general_info(cached_data):
	print "\n ### HELP: Try filtering by these categories (type 'python script.py _ONE_OF_THESE_'):"
	row_counter = 0.
	counter = 0
	for row in cached_data:
		if row_counter == 0:
			for field in row:
				print "%d) %s" % (counter + 1, field)
				counter += 1
			row_counter += 1
		else:
			return 0


def get_stats(cached_data, search_field):
	try:
			column_found = 0
			row_counter = 0.
			chosen_column = 0
			for row in cached_data:
				if row_counter == 0:
					initial_counter = 0
					for column in row:
						if column.lower() == search_field.lower():
							column_found = 1
							chosen_column = initial_counter
						initial_counter += 1
					row_counter += 1
				elif column_found == 1:
					result = row[chosen_column]
					if result in column_dictionary:
						column_dictionary[result] += 1
					else:
						column_dictionary[result] = 1
					row_counter += 1
				else:
					row_counter += 1
			return row_counter
	except IOError:
		print "IOERROR is raised. Are you sure you are in the right folder? We couldn't find the file you gave us.\n\n"
		exit(1)

#end get stats

def run_stats(cached_data, search_field):
	#get_stats
	row_counter = get_stats(cached_data, search_field)

	if column_dictionary == {}:
		print "WARNING: no results found (run stats)"
	else:
		final_list = []
		for key, value in sorted(column_dictionary.iteritems(), key=lambda (k,v): (v,k)):
		    final_list.append('%s: %s of %d  (%.2f percent)' % (key, value, row_counter, value / row_counter * 100 ))
		final_list.reverse()
		for item in final_list:
			print item 

#end run stats


def get_breakdown(cached_data, search_field):
	row_counter = get_stats(cached_data, search_field)
	if column_dictionary == {}:
		print "WARNING: no results found (get_breakdown)"
	else:
		print "\n ### HELP: Try filtering by these answers to the category (type 'python script.py _CATEGORY_ %s _ONE_OF_THESE_'):" % (search_field)
		counter = 0
		for key in column_dictionary:
			print "%d) %s" % (counter + 1, key)
			counter += 1

#end get breakdown


ret_file = "tally-results.csv"
 
file_to_search = "data.csv"
cached_data = load_data(file_to_search)
	
search_field = ""
filter_field = ""
filter_value = ""

column_dictionary = {}

arg_length = len(sys.argv)
print arg_length
if(arg_length == 1):
	general_info(cached_data)
	sys.exit()
else:
	if(arg_length >= 2):
		search_field = sys.argv[1]
		if arg_length == 2 and sys.argv[1] == "help":
			general_info(cached_data)
			sys.exit()
		elif(arg_length == 3):
			if sys.argv[1] == "help":
				get_breakdown(cached_data, sys.argv[2])
				sys.exit()

#iterator for multiple filters		
if(arg_length >= 4):
	search_field = sys.argv[1]
	i = 2
	while i < arg_length:
		filter_field = sys.argv[i]
		filter_value = sys.argv[i+1]
		found_column = find_column(cached_data, filter_field)
		cached_data = filter_data(cached_data, found_column, filter_value)
		i += 2

#end iterator

run_stats(cached_data, search_field)


"""print '\nTrying to write new file to ' + ret_file + '\n'

with open(ret_file, 'w+') as writefile:
	csv_writer = csv.writer(writefile)
	for row in ret_contents:
			csv_writer.writerow(row)

print 'Results should all be written in ' + ret_file"""

