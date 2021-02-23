from euler import euler
import math

a = True
while a:
	dxdy = input("Type in dy/dx: ")
	dxdy = "dydx = lambda x,y: " + dxdy
	try:
		exec(dxdy)
		a = False
	except:
		print("Check your function")

boundary = tuple(map(float, input("Type in (x,y) starting point: ").split(',')))
iterations = int(input("Iterations: "))
step = input("Step size: ")
prec = len(step) - 2
step = float(step)

for i in euler(dydx, boundary, iterations, step, prec):
	print(i)

input()