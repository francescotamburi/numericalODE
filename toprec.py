def to_precision(x,p):
	x = round(x, p)
	x = str(x)
	l = len(x)
	d = 0
	for i in x:
		if i == ".": 
			break
		else:
			d+=1
	
	if d == l:
		x = x + "." + "0"*p
	elif l-d-1 < p:
		x = x + "0"*(p-(l-d-1))
		
	return(x)

print(to_precision(0.12,3))