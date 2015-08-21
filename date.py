
import random
from random import randint
import datetime
from datetime import timedelta
import time

base = datetime.datetime.today()
final_date =  base - datetime.timedelta(365)
next_date = final_date - datetime.timedelta(2)



# while in range of a year
while next_date  < base:

	next_date = next_date + datetime.timedelta(randint(1,3))
	print next_date.strftime("%Y-%m-%d")
	
	# next_date = str(next_date.strptime('24052010', '%d%m%Y').date())
	p_days = randint(4,6)
	print "start of period: ", str(next_date.strftime("%Y-%m-%d"))
	#enter period for (+/- 1 days)
	for i in range(1,p_days):
		day = next_date + datetime.timedelta(i)
		print "period day: ", str(day.strftime("%Y-%m-%d"))
	# add 28 (+/- 1-7 days)
	next_date = next_date  + datetime.timedelta(randint(26,29))
	print "next expected period: ", str(next_date.strftime("%Y-%m-%d")), "\n"
