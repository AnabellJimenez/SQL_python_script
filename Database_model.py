'''Python script to generate SQL tables and data for the fertility app simulation/functional testing'''

import sqlite3
import datetime
from datetime import datetime

class Database():
	def __init__(self, db_file):
		self.db_file = db_file
		self.db = self.open()

	def open(self):
		return sqlite3.connect(self.db_file)

	def close(self):
		return self.db.close()

	def read_user(self):
		self.cursor = self.db.cursor()
		self.cursor.execute('''SELECT*FROM user''')
		table_list = self.cursor.fetchall()
		return table_list
		self.db.commit()

	def read_mood(self):
		self.cursor = self.db.cursor()
		self.cursor.execute('''SELECT*FROM mood''')
		table_list = self.cursor.fetchall()
		return table_list
		self.db.commit()

	def read_symptoms(self):
		self.cursor = self.db.cursor()
		self.cursor.execute('''SELECT*FROM symptoms''')
		table_list = self.cursor.fetchall()
		return table_list
		self.db.commit()

	def read_intercourse(self):
		self.cursor = self.db.cursor()
		self.cursor.execute('''SELECT*FROM intercourse''')
		table_list = self.cursor.fetchall()
		return table_list
		self.db.commit()

	def print_read(self, list_tuples):
		for item in list_tuples:
			print item

	def create_user(self, first_name, last_name, age):
		self.cursor = self.db.cursor()
		self.cursor.execute(
			'''INSERT INTO user(first_name, last_name, age) VALUES(?,?,?)''', (first_name, last_name, age))
		id_user = self.cursor.lastrowid
		self.db.commit()
		return id_user

	def period(self, user_id, date_created, select_val):
		self.cursor = self.db.cursor()
		self.cursor.execute(
			'''INSERT INTO period(user_id, date_created, select_val) VALUES(?,?,?)''', (user_id, date_created, select_val))
		id_entry = self.cursor.lastrowid
		self.db.commit()
		return id_entry

	def intercourse(self, user_id, date_created, select_val):
		self.cursor = self.db.cursor()
		self.cursor.execute(
			'''INSERT INTO intercourse(user_id, date_created, select_val) VALUES(?,?,?)''', (user_id, date_created, select_val))
		id_entry = self.cursor.lastrowid
		self.db.commit()
		return id_entry

	def mood(self, user_id, date_created, select_val):
		self.cursor = self.db.cursor()
		print "MOOD In DB: ", user_id,date_created,select_val
		self.cursor.execute(
			'''INSERT INTO mood(user_id, date_created, select_val) VALUES(?,?,?)''', (user_id, date_created, select_val))
		id_entry = self.cursor.lastrowid
		self.db.commit()
		return id_entry

	def cervical_fluid(self, user_id, date_created, select_val):
		self.cursor = self.db.cursor()
		self.cursor.execute(
			'''INSERT INTO cervical_fluid(user_id, date_created, select_val) VALUES(?,?,?)''', (user_id, date_created, select_val))
		id_entry = self.cursor.lastrowid
		self.db.commit()
		return id_entry

	def log_in(self, user_id, date_created):
		self.cursor = self.db.cursor()
		self.cursor.execute(
			'''INSERT INTO log_in(user_id, date_created) VALUES(?,?)''', (user_id, date_created))
		id_entry = self.cursor.lastrowid
		self.db.commit()
		return id_entry

	def ovulation_test(self, user_id, date_created, select_val):
		self.cursor = self.db.cursor()
		self.cursor.execute(
			'''INSERT INTO ovulation_test(user_id, date_created, select_val) VALUES(?,?,?)''', (user_id, date_created, select_val))
		id_entry = self.cursor.lastrowid
		self.db.commit()
		return id_entry

	def pregnancy_test(self, user_id, date_created, select_val):
		self.cursor = self.db.cursor()
		self.cursor.execute(
			'''INSERT INTO pregnancy_test(user_id, date_created, select_val) VALUES(?,?,?)''', (user_id, date_created, select_val))
		id_entry = self.cursor.lastrowid
		self.db.commit()
		return id_entry

	def symptoms(self, user_id, date_created, select_val):
		self.cursor = self.db.cursor()
		self.cursor.execute(
			'''INSERT INTO symptoms(user_id, date_created, select_val) VALUES(?,?,?)''', (user_id, date_created, select_val))
		id_entry = self.cursor.lastrowid
		self.db.commit()
		return id_entry

	def weight(self, user_id, date_created, entry):
		self.cursor = self.db.cursor()
		self.cursor.execute(
			'''INSERT INTO weight(user_id, date_created, entry) VALUES(?,?,?)''', (user_id, date_created, entry))
		id_entry = self.cursor.lastrowid
		self.db.commit()
		return id_entry

	def sleep(self, user_id, date_created, entry):
		self.cursor = self.db.cursor()
		self.cursor.execute(
			'''INSERT INTO sleep(user_id, date_created, entry) VALUES(?,?,?)''', (user_id, date_created, entry))
		id_entry = self.cursor.lastrowid
		self.db.commit()
		return id_entry

	def basal_temp(self, user_id, date_created, entry):
		self.cursor = self.db.cursor()
		self.cursor.execute(
			'''INSERT INTO basal_temp(user_id, date_created, entry) VALUES(?,?,?)''', (user_id, date_created, entry))
		id_entry = self.cursor.lastrowid
		self.db.commit()
		return id_entry

	def activity(self, user_id, date_created, entry, select_val):
		self.cursor = self.db.cursor()
		self.cursor.execute(
			'''INSERT INTO activity(user_id, date_created, entry, select_val) VALUES(?,?,?, ?)''', (user_id, date_created, entry, select_val))
		id_entry = self.cursor.lastrowid
		self.db.commit()
		return id_entry

	def nutrition(self, user_id, date_created, entry, select_val):
		self.cursor = self.db.cursor()
		self.cursor.execute(
			'''INSERT INTO nutrition(user_id, date_created, entry, select_val) VALUES(?,?,?, ?)''', (user_id, date_created, entry, select_val))
		id_entry = self.cursor.lastrowid
		self.db.commit()
		return id_entry

	def get_user_list(self):
		self.cursor = self.db.cursor()
		self.cursor.execute('''SELECT*FROM user''')
		table_list = self.cursor.fetchall()
		return table_list
		self.db.commit()
		
'''function calls to test tables are created and information is entered properly'''
# db = Database("fertility")
# # print db.create_user("Janet", "Jackson", 45)
# # print db.intercourse(2, str(datetime.now()) ,1)
# print db.nutrition(8, str(datetime.now()),1, 2)
# db.print_read(db.read_table())