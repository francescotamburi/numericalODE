import sys
import math
import euler

#lambda f(x), x, previous y, current y, step
def predictor(f, x, prev, curr, h):
	return curr + h*(3*f(x,curr) - f(x-step, prev))/2

#lambda f(x), x, previous y, current y, step
def corrector(f, x, curr, subs, h):
	return curr + h*((x,curr) + f(x+step, subs))/2

def predictor_corrector(fp, b, t, h, p):
	"""
	tuple b   = coordinates of boundary condition (x0, y0)
	float h   = step
	int t     = number of steps
	lambda fp = dy/dx
	int p     = significant digits after x values
	"""
	
	ret = euler.euler(fp,b, 1, h, p)
	x = b[0]
	
	for i in range(1, t):
		x = round(x + h, p)
		yt = predictor(fp, x, ret[i][1], ret[i-1][1], h)
		y  = predictor(fp, x, ret[i][1], yt, h)
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
		for i in predictor_corrector(dydx, boundary, iterations, step, prec):
			print(i)