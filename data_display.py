import sqlite3
'''Python file to enter sql code into command line and generate a csv file with the information from the: fertility SQL DB '''

from Database_model import Database
import requests
import csv

#open sqlite3 connection
def db_open(filename):
	return sqlite3.connect(filename)

#close sqlite3 connection
def db_close(conn):
	conn.close()

#function takes an SQL command as a parameter and returns what is in the table
def db_select(conn, SQL_cmd):
	c = conn.cursor()
	c.execute(SQL_cmd)
	return c.fetchall()

#function opens file, taking in filename and data list as paramter and writes to a CSV
def open_file(filename, data_list):
	with open(filename, "wb") as f:
		csv_writer = csv.writer(f)
		for data in data_list:
			csv_writer.writerow(data)


'''function calls 
***BUG: HEADER IN CSV FILE!!!!

'''

conn = db_open("fertility")
filename = raw_input("Enter file you want to create: ")
SQL_cmd = raw_input("Enter SQL command you want to execute: \n")
data_list = db_select(conn, SQL_cmd)
open_file(filename, data_list)


# def read_file(filename):
# 	with open(filename, "r") as f:
# 		lines = f.readlines()
# 		# print lines
# 	array = []
# 	for line in lines:
# 		# line.split(",")
# 		# print line
# 		line.split(",")
# 		line[0].strip("\n")
# 		line[1].strip("\n")
# 		new_hash = {}
# 		new_hash["x"]=line[0]
# 		new_hash["y"]=line
# 		array.append(new_hash)
# 	return array
