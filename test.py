import sys
import math

if __name__ == "__main__":
	if sys.argv[1] == "help" or sys.argv[1] == "h":
		print('"f(x)", x0, iterations, step-size')
	else:
		dydx = sys.argv[1]
		dydx = "dydx = lambda x: " + dydx
		exec(dydx)
		x = float(sys.argv[2])
		iterations = int(sys.argv[3])
		step = sys.argv[4]
		prec = len(step) - 2
		step = float(step)
		
		for i in range(iterations+1):
			print((x, dydx(x)))
			x = round(x + step, prec)