import datetime

MAX_SCORE = 31.0

def age_score (age):
	if age < 20:
		return 1
	elif age < 30:
		return 2
	else: return 3

#def nova ():
#	print age_score(10)

#def display_age(age):
#	print age

def fb_score(num_FB_friends):
	if num_FB_friends < 100:
		return 1
	elif num_FB_friends < 200:
		return 2
	else: return 3

def deadlines_score (deadlines):
	if deadlines == "Yes":
		return 3
	else: return 0

def bus_score (missed_busses):
	if missed_busses > 0:
		return 3
	else: return 0

def family_score (num_family):
	if num_family < 3:
		return 1
	elif num_family < 5:
		return 2
	else: return 3

def job_score (job):
	if job > 6:
		return 1
	elif job > 3:
		return 2
	else: return 3

def temp_score (temp):
	if temp >30 & temp <10:
		return 3
	else: return 0

def internet_speed_score (internet_speed):
	if internet_speed == "very":
		return 10
	else: return 0


def calculate_complexity(age, num_FB_friends, deadlines, missed_busses, num_family, job, temp, internet_speed):
	score=fb_score(num_FB_friends) + age_score(age) + deadlines_score (deadlines) + bus_score (missed_busses) + family_score (num_family) + job_score (job) + temp_score (temp) + internet_speed_score (internet_speed)
	
	print "Your life complexity is:", score
	print "Real feel:", 100 * score / MAX_SCORE



age = raw_input("How old are you? ")
num_FB_friends = raw_input("How many FB friends do you have? ")
deadlines = raw_input("Do you have any deadlines? ")
missed_busses = raw_input("How many busses did you missed? ")
num_family = raw_input("How many family members do you have? ")
job = raw_input("On scale 1-10, how do you like your job ")
temp = raw_input("What is outside temperature? ")
internet_speed = raw_input("How slow is your internet connection? ")

#int(age)   typecasting

calculate_complexity(int(age), int(num_FB_friends), deadlines, int(missed_busses), int(num_family), int(job), int(temp), internet_speed)

datum = datetime.datetime.today() # datum
datum = datetime.datetime.now() #datum in ura 



