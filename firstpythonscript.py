
import numpy as np
import sympy as sp

x ,t = sp.symbols('x t')

poly = sp.expand((x-2)*(t+3))

print(poly.subs({x:2,t:1}))

# Eulers Method w/ User's Choice of ODE

