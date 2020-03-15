for i in range(1,101):
	a = i%10
	b = (i-a)/10
	if i%7 == 0:
		continue
	elif a ==7 or b ==7:
		continue
	else:
		print("{}".format(i))
