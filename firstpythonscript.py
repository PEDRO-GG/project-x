
import numpy as np
import sympy as sp

t, y = sp.symbols("y t")

UserODE = input("Enter ODE (in terms of t & y): y' =  ")

ODE = sp.sympify(UserODE)

variables = (ODE.free_symbols)


if t in variables and y in variables:
    t0= int(input('write an initial point for t(to): '))
    y0= int(input('write an initial point for y(yo): '))
    InitODE = ODE.subs({t:t0,y:y0})




# Display the identified ODE at certain pts.
print("The variables in the function are:", InitODE)


# Eulers Method w/ User's Choice of ODE

