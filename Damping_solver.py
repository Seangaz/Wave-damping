from scipy.optimize import fsolve
import numpy as np
T = 6.1047
L =  0.3
f = 215.8
mass = 0.4
m = 0.0008 + mass
mu =  0.0009163802978
def solve(ζ):
    return ((np.sqrt(1 - ζ**2)*T)/(8*mu*f**2*L**2)+np.pi/4-(ζ**2*np.pi)/4-ζ-0.0000575/(np.pi*mu)-1.03*m/(np.pi*mu*f**2*L**2))
initial_guess = 0.5
damping_ratio = fsolve(solve, initial_guess)
print("Calculated damping ratio ζ =", round(damping_ratio[0], 6))
