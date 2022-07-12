#Python program to solve quadratic equation

import cmath
a = 2
b = 2
c = 2
d = (b**2) - (4*a*c)
sol1 = (-b - cmath.sqrt(d)/(2*a))
sol2 = (-b + cmath.sqrt(d)/(2*a))
print('The solution of the quadratic equation are {0} and {1}'.format(sol1,sol2))
