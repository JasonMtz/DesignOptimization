
import numpy
from sympy import symbols, diff
x, y = symbols('x y')
function = 2*x**2 - 4*x*y + 1.5*y**2 +y

gradient = [4*x - 4*y , -4*x + 3*y+1]

eps = 1e-3  # termination criterion
y = [0] # initial guess
x = [0]
k = 0  # counter
soln = [x, y]
error = numpy.linalg.norm(gradient)
# a = 0.01  # set a fixed step size to start with

# Armijo line search
def line_search(x):
    a = 1.  # initialize step size
    phi = lambda a, x: function - a * 0.8 * gradient ** 2  # define phi as a search criterion
    while phi(a, x) < function(x - a * gradient):  # if f(x+a*d)>phi(a) then backtrack. d is the search direction
        a = 0.5 * a
    return a


while error >= eps:  # keep searching while gradient norm is larger than eps
    a = line_search(x)
    x = x - a * gradient
    soln.append(x, y)
    error = numpy.linalg.norm(gradient)

soln  # print the search trajectory
