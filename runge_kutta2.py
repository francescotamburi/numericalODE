import sys
import math

def runge_kutta2(f2p, b, t, h, p):
	"""
	tuple b    = coordinates of boundary condition (x0, y0)
	float h    = step
	int t      = number of steps
	lambda f2p = d2y/dx2
	int p      = significant digits after x values
	"""
	
	x   = b[0]
	y   = b[1]
	yp  = b[2]
	y2p = f2p(x,y,yp)
	ret = [(x, y)]     #list of tuples to be returned with x and the associated y values
	
	for i in range(0, t):
		k1 = h**2/2 * f2p(x,     y,                 yp)
		k2 = h**2/2 * f2p(x+h/2, y + h*yp/2 + k1/4, yp + k1/h)
		k3 = h**2/2 * f2p(x+h/2, y + h*yp/2 + k1/4, yp + k2/h)
		k4 = h**2/2 * f2p(x+h  , y + h*yp   + k3  , yp + 2*k3/h)
		P  = (k1 +   k2 +   k3)/3
		Q  = (k1 + 2*k2 + 2*k3 + k4)/3
		y  = y  + h*yp + P
		yp = yp + Q/h 
		x = round(x + h, p)
		ret.append((x,y))
	
	return ret

if __name__ == "__main__":
	if sys.argv[1] == "help" or sys.argv[1] == "h":
		print('"f\"(x,y)", "x0,y0,yp", iterations, step-size')
	else:
		d2ydx2 = sys.argv[1]
		d2ydx2 = "d2ydx2 = lambda x,y,yp: " + d2ydx2
		exec(d2ydx2)
		boundary = tuple(map(float, sys.argv[2].split(',')))
		iterations = int(sys.argv[3])
		step = sys.argv[4]
		prec = len(step) - 2
		step = float(step)
		for i in runge_kutta2(d2ydx2, boundary, iterations, step, prec):
			print(i)