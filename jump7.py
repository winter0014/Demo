for x in range(1,101):
	if x%7 == 0:
		continue
	elif int(x/10) == 7 or int(x%10) == 7:
		continue
	else :
		print(x)