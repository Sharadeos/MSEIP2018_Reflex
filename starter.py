#Starter code to import the CSV file

import csv


with open('setosa_v_versicolor.csv', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	
	for row in csvreader:
		slength = row[0]