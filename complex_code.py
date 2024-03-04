####--------------------------------------------------------####
import numpy as np
import matplotlib.pyplot as plt

def odeEuler(f,y0,t):
    y = np.zeros(len(t))
    y[0] = y0
    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1] - t[n])
    return y



#t = np.linspace(-0.5, 2,101)
#y0 = 0
#f = lambda y, t: np.exp(t) * np.sin(t)
#y = odeEuler(f, y0, t)

#y_true = ((np.exp(t)*np.sin(t)) - (np.exp(t)*np.cos(t)))/2
#mostly use to plot grahf
"""plt.plot(t, y, 'b.-', label='Numerical solution (Euler)')
plt.plot(t, y_true, 'g-', label='Exact solution')
plt.legend()
plt.axis([0, 2, 0, 6])
plt.xlabel('time (s)')
plt.ylabel('Distance (m)')
plt.grid(True)
plt.title("Solution of $y' = e^t \\sin(t), \\quad y(0) = 1$")
plt.show()"""
####---------------------------------------------------------####

import sympy as sp
t = sp.symbols("t") #create symbols 
f1= 24*sp.exp(-0.22*t) #function
f2 = t**2
change_rate = sp.integrate(f1, (t, 0, 5)) #t is symbols, 0 is number when write integrate is down number, 1 is upper number For integrate
diffting =sp.diff(f2,t)#For diff
print(diffting)

#Use the diff() function to take the derivative.

#Use solveset() to solve for critical points.

#Create a list containing the critical points and interval endpoints.

#Use the subs() function with a list comprehension to compute derivative values at critical points and endpoints.

#Compare values to find global maximum and minimum.

#solve equation
k = sp.symbols('k')
pop = sp.Eq(2+k,8)
pp = sp.solve(pop,k,domain=sp.S.Reals)
print(pp)
####-----------------------------------####
def odie(): #solve complex eqaution (better than ode rule)
    import numpy as np
    from scipy.integrate import odeint
    import matplotlib.pyplot as plt

    # https://scipy.org/
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html
    # ODE Function dy/dt = k.t = f(t)
    # Integrate (k.t)dt = k.(t^2)/2 + C 
    # C = Constant
    # To find C, if k = 2; Equation y(t) = t^2 + C
    # Initial condition (t0,y0) = (0,1), t0 = 0, y0 = 1; 
    # Substitute; y(t0) = 1 = 0 + C, therefore, C = 1
    # Exact solution: y_exac(t) = t^2 + 1
    def model(y,t):
        k = 2.0
        dydt = k*t    
        return dydt

    k = 2.0
    dydt = k*t    


    # Initial condition
    y0 = 1

    # Time points
    t_start = 0
    t_stop = 20
    t_step = 100
    t = np.linspace(t_start,t_stop,t_step)

    # Solve ODE using ODEINT
    y_cal = odeint(model,y0,t)
    y_exac = t**2+1

    # Plot results as y = f(t)
    plt.plot(t,y_cal,'yo')
    plt.plot(t,y_exac,'k+')
    plt.xlabel('time [sec]')
    plt.ylabel('y_cal(t) vs. y_exac(t)')
    plt.legend(["y_cal_ode", "y_exact"], loc ="lower right") 
    plt.show()
    return 