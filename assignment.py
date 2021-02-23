import euler
import eulercauchy
import runge_kutta
import math

#dydx  = lambda x,y: x*(5-3*y)/(1+x**2)
#fex   = lambda   x: (2*math.sqrt(2)/(1+x**2)**(3/2)+5)/3

dydx  = lambda x,y: (2*y-2)/x
fex   = lambda   x: (x**3+1)

def to_precision(x,p):
	x = round(x, p)
	x = str(x)
	
	if "e-" in x:
		n = x.split("e-")
		n[1] = int(n[1])
		x = "0." + "0"*(n[1]-1) +n[0]
		
	
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
	

def formatter(numerical, exact, eprec):
	ret = []
	c = 0
	for i in numerical:
		x = i[0]
		y = i[1]
		e = exact[c]
		error = abs(y-e)/e * 100
		error = to_precision(error, eprec)
		y = to_precision(y, 5)
		e = to_precision(e, 5)
		ret.append((to_precision(x,1),y,e,error))
		c+=1
	
	return ret

h = 0.2
x0 = x = 1
y0 = fex(1)
step = 20
exact = []

for i in range(step+1):
	exact.append(fex(x))
	x = round(x+h, 1)

f = open("methods.csv", "w")

try:
	f.write("x, y(euler), y(exact), %error \n")
	for i in formatter(euler.euler(dydx, (x0,y0), 20, h, 1), exact, 2):
		f.write(f"{i[0]},{i[1]},{i[2]},{i[3]}\n")
	
	f.write("\n")
	
	f.write("x, y(e_cauchy), y(exact), %error \n")
	for i in formatter(eulercauchy.euler_cauchy(dydx, (x0,y0), 20, h, 1), exact, 2):
		f.write(f"{i[0]},{i[1]},{i[2]},{i[3]}\n")
	
	f.write("\n")
	
	f.write("x, y(r_kutta), y(exact), %error \n")
	for i in formatter(runge_kutta.runge_kutta(dydx, (x0,y0), 20, h, 1), exact, 5):
		f.write(f"{i[0]},{i[1]},{i[2]},{i[3]}\n")
finally:
	f.close()