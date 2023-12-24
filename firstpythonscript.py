
import numpy as np
import sympy as sp

x = sp.symbols('x')

poly = sp.expand((x-2)*(x+3))

print(poly)