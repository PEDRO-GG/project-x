

import numpy as np
import sympy as sp
import matplotlib.pyplot as mp

t, y = sp.symbols("t y")


UserODE = input("Enter ODE (in terms of t & y): y' =  ")

if 'e' in UserODE:
    ModUserODE = UserODE.replace('e',str(sp.E))  # If D.E has an Eulers Number,
    ODE = sp.sympify(ModUserODE)                 # then it'll adjust to eval. e
else:
    ODE = sp.sympify(UserODE)

variables = (ODE.free_symbols)


if t in variables or y in variables:
    t0= float(f"{float(input('write the initial point, t0 = ')):.{4}f}")
    y0= float(f"{float(input('And now y(t0) = y0 = ')):.{4}f}")
    InitODE = ODE.subs({t:t0,y:y0})

# Euler's method

# Finding an answer to solution of ODE
yoft = float(f"{float(input('Up to what y(t) do you want an answer?(choose t for y(t)): ')):.{4}f}")
h = float(f"{float(input('what step size do you want?: ')):.{4}f}")

t_ = np.arange(t0, yoft + h ,h)
ysol = []
for i in t_:
    yn = y0 + h * ODE.subs({t:i,y:y0})
    ysol.append(yn)
    y0 = yn

print(f"at t = {yoft} , y({yoft}) = {(round(yn, 3))}")

# Eulers Method w/ User's Choice of ODE

## Plugging in true soln. to 
# see accuracy of the method

print("Error Analysis: ")
tru = input("Input true solution: ")

if 'e' in tru:
    true = tru.replace('e',str(sp.E))  # If D.E has an Eulers Number,
    true = sp.sympify(true)
else:
    true = sp.sympify(tru)
ypts =[]
for i in t_:
    ytrue = true.subs({t:i})
    ypts.append((ytrue))

mp.plot(t_,ysol,label= "Numerical Soln")
mp.plot(t_,ypts,label= "True Soln")
mp.xlabel("t")
mp.ylabel("y")
mp.legend()
mp.show()