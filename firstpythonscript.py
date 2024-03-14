

import numpy as np
import sympy as sp
from test import EulersMethod

t, y = sp.symbols("t y")


UserODE = input("Enter ODE (in terms of t & y): y' =  ")

if 'e' in UserODE:
    ModUserODE = UserODE.replace('e',str(sp.E))  # If D.E has an Eulers Number,
    ODE = sp.sympify(ModUserODE)                 # then it'll adjust to eval. e
else:
    ODE = sp.sympify(UserODE)

variables = (ODE.free_symbols)


if t in variables and y in variables:
    t0= float(f"{float(input('write the initial point, t0 = ')):.{4}f}")
    y0= float(f"{float(input('And now y(t0) = y0 = ')):.{4}f}")
    

# Euler's method

# Finding an answer to solution of ODE
yoft = float(f"{float(input('Up to what y(t) do you want an answer?(choose t for y(t)): ')):.{4}f}")
h = float(f"{float(input('what step size do you want?: ')):.{4}f}")

t_n = np.arange(t0, yoft + h ,h)

EulersMethod(t_n,h,y0,ODE)

print(" at t = " + str(yoft) + ", y(" + str(yoft) + ")=" + str(EulersMethod(t_n,h,y0,ODE))  )

# Eulers Method w/ User's Choice of ODE

