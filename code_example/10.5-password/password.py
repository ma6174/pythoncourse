#rje
# updated, wfp, using while
# updated rje 5/15/12 Python 3
# Three tries to get a password
# Demo "break", "continue", and "while"


passwdList = ["bad", "BetTeR", "Ev3n_B3tT3r-p455wd"]
valid = False
cnt = 3  # count of number of attempts
while cnt > 0:
	input_str = input("Enter password: ")
	for passwd in passwdList:  # check input against all passwords
		if input_str == passwd:
			valid = True
			break   # break out of "for"
	if not valid:
		cnt = cnt - 1
		print("Bad password. Try again. You have", cnt, "tries remaining")
		continue  # go directly to top of loop
	else:
		break  # break out of "while"
if cnt > 0:
	print("Password Accepted")
else:
	print("Password Rejected")
