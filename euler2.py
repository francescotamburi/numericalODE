import sys
import math

def euler2(f2p, b, t, h, p):
	"""
	tuple b   = boundary condition (x0, y0, y'0)
	float h   = step
	int t     = number of steps
	lambda f2p = dy/dx
	int p     = significant digits after x values
	"""
	
	x   = b[0]
	y   = b[1]
	yp  = b[2]
	y2p = f2p(x, y, yp)
	ret = [(x, y)]     #list of tuples to be returned with x and the associated y, y' and y" values
	
	for i in range(0, t):
		x   = round(x + h, p)
		y   = y  + h * yp  + h**2 * y2p / 2
		yp  = yp + h * y2p 
		y2p = f2p(x, y, yp)
		ret.append((x,y))
	
	return ret

if __name__ == "__main__":
	if sys.argv[1] == "help" or sys.argv[1] == "h":
		print('"f\"(x)", "x0,y0,y\'0", iterations, step-size')
	else:
		dy2d2x = sys.argv[1]
		dy2d2x = "dy2d2x = lambda x,y,yp: " + dy2d2x
		exec(dy2d2x)
		boundary = tuple(map(float, sys.argv[2].split(',')))
		iterations = int(sys.argv[3])
		step = sys.argv[4]
		prec = len(step) - 2
		step = float(step)
		for i in euler2(dy2d2x, boundary, iterations, step, prec):
			print(i)