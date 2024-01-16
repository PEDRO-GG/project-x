# Eulers Method Function
import sympy as sp
t, y = sp.symbols("t y")

def EulersMethod(t_n,h,y0,ode):
    for i in t_n:
        yn = y0 + h * ode.subs({t:i,y:y0})
        y0 = yn
    return yn