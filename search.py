""" This module is used to search csv files"""

import csv

""" returns a list of lists where the sublists are all the rows of the CSV """
def getRows(csv_file):
	rows = []
	try:
		# open file in "universal new-line mode" so that it handles empty excel cells better
		with open(csv_file, 'rU') as csvfile:
			csv_reader = csv.reader(csvfile)
			for row in csv_reader:
				rows.append(row)
	except IOError:
		print "IOERROR is raised. File probably not in directory\n\n"
		exit(1)
	return rows


""" returns a list of lists where the sublists are all the columns of the CSV """
def getCols(csv_file):
	cols = []
	try:
		# open file in "universal new-line mode" so that it handles empty excel cells better
		with open(file_to_search, 'rU') as csvfile:
			csv_reader = csv.reader(csvfile)
			i = 0
			for row in csv_reader:
				for index in xrange(row):
					if (i == 0):
						cols.append([row[index]])
					else:
						cols[index].append(row[index])
			i += 1
	except IOError:
		print "IOERROR is raised. Are you sure you are in the right folder? We couldn't find the file you gave us.\n\n"
		exit(1)
	return cols

""" Take a .csv file, return all rows that include any of the expressions in the input list exps """
def findAllContaining(csv_file, exps):
	dataRows = getRows(csv_file)
	retRows = []
	for row in dataRows:
		added = False
		for cell in row:
			if not added:
				for exp in exps:
					if exp in cell:
						retRows.append(row)
						added = True
	return retRows

""" Take a set of rows, save to .csv file with file name as input fileName """
def saveRowsToCSV(rows, fileName):
	with open(fileName, 'w+') as writefile:
		csv_writer = csv.writer(writefile)
		for row in rows:
				csv_writer.writerow(row)




