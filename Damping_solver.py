from scipy.optimize import fsolve
import numpy as np
T = 0
L =  0
f = 0
mu =  0
def solve(ζ):
    return ((np.sqrt(1 - ζ**2)*T)/(8*mu*f**2*L**2)+np.pi/4-(ζ**2*np.pi)/4-ζ)
initial_guess = 0.1
damping_ratio = fsolve(solve, initial_guess)
print("Calculated damping ratio ζ =", damping_ratio[0])
