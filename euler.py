import sys
import math

def euler(fp, b, t, h, p):
	"""
	tuple b   = coordinates of boundary condition (x0, y0)
	float h   = step
	int t     = number of steps
	lambda fp = dy/dx
	int p     = significant digits after x values
	"""
	
	x   = b[0]
	y   = b[1]
	ret = [(x, y)]     #list of tuples to be returned with x and the associated y values
	
	for i in range(0, t):
		yp = fp(x, y)
		x = round(x + h, p)
		y = y + h * yp
		ret.append((x,y))
	
	return ret

if __name__ == "__main__":
	if sys.argv[1] == "help" or sys.argv[1] == "h":
		print('"f\'(x)", "x0,y0", iterations, step-size')
	else:
		dydx = sys.argv[1]
		dydx = "dydx = lambda x,y: " + dydx
		exec(dydx)
		boundary = tuple(map(float, sys.argv[2].split(',')))
		iterations = int(sys.argv[3])
		step = sys.argv[4]
		prec = len(step) - 2
		step = float(step)
		for i in euler(dydx, boundary, iterations, step, prec):
			print(i)