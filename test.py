
import numpy as np
import sympy as sp
from EulerMethod import EulersMethod


t, y = sp.symbols("t y")




# Testing EulerMethod Function
# 1. y' = t - y + 1 w/ y(0) = 1, where we want y(2)  
t0_1 = 0
y0_1 = 1
yt_1 = 3
h1 = .0001
t_n1 = np.arange(t0_1,yt_1 + h1,h1)

ODE_1 = 't - y + 1'
ODESOLN_1 = '(e**-t) + t'

if 'e' in ODE_1 or 'e' in ODESOLN_1:
    ModUserODE = ODE_1.replace('e',str(sp.E))
    ModUserODE1 = ODESOLN_1.replace('e',str(sp.E))  # If D.E has an Eulers Number,
    ODE1 = sp.sympify(ModUserODE)  
    ODESOLN1 = sp.sympify(ModUserODE1)
else:
    ODE1 = sp.sympify(ODE_1)
    ODESOLN1 = sp.sympify(ODESOLN_1)

test1 = float(f"{EulersMethod(t_n1, h1, y0_1, ODE1):.{3}f}")
proofof1= float(f"{ODESOLN1.subs({t:(yt_1)}):.{3}f}")


if test1 != proofof1:
    print("test 1 fail")
else:
    print('test 1 succesful')

# 2. y' = (3t^2 + 2t - 6)/2y w/ y(1) = 3, where we want y(2)  
t0_2 = 1
y0_2 = 3
yt_2 = 2
h2 = .0001
t_n2 = np.arange(t0_2,yt_2 + h2,h2)

ODE_2 = '(3*(t**2) + 2*t + 6) / (2*y)'
ODESOLN_2 = 'sqrt(t**3 + t**2 + 6*t +1)'

if 'e' in ODE_2 or 'e' in ODESOLN_2:
    ModUserODE = ODE_2.replace('e',str(sp.E))
    ModUserODE1 = ODESOLN_2.replace('e',str(sp.E))  # If D.E has an Eulers Number,
    ODE2 = sp.sympify(ModUserODE)  
    ODESOLN2 = sp.sympify(ModUserODE1)           # then it'll adjust to eval. e
else:
    ODE2 = sp.sympify(ODE_2)
    ODESOLN2 = sp.sympify(ODESOLN_2)


test2 = float(f"{EulersMethod(t_n2, h2, y0_2, ODE2):.{3}f}")
proofof2 = float(f"{ODESOLN2.subs({t:(yt_2)}):.{3}f}")


if test2 != proofof2:
    print("test 2 fail")
else:
    print('test 2 succesful')







