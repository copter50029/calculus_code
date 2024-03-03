'''Solving PDE of heat conduction equation (Parbolic)'''
import numpy as np
import matplotlib.pyplot as plt
 
# Define distance space (dx = h) and time step (dt = k)
h = 0.025; k = 0.02
x = np.arange(0,1+h,h)
t = np.arange(0,0.1+k,k)

# Boundary Condition (B.C)
BC = [0,0]

# Initial Condition (I.C)
IC = np.sin(np.pi*x)

n = len(x); m = len(t)
T = np.zeros((n,m))

#Assign values for Boundary conditions (B.C.)
T[0,:] = BC[0]; T[-1,:] = BC[1]

#Assign values for Initial conditions (I.C.)
T[:,0] = IC
T.round(3)

# Define coefficients coff = k/h^2
coeff = k/(h**2)


# Apply explict finit difference method to calculate T(i,j)
for j in range(1,m):
    for i in range (1,n-1):
        T[i,j] = coeff*T[i-1,j-1] + \
                 (1-2*coeff)*T[i,j-1] + \
                 coeff*T[i+1,j-1]
T.round(3)

# Plot approximate solution of PDE
R = np.linspace(1,0,m)
B = np.linspace(0,1,m)
G = 0

for j in range (m):
    plt.plot(x,T[:,j], color=[R[j],G,B[j]])
    
#plt.plot(T)
plt.legend(t)
plt.title('Temperature distribution T(x,t) of metal rod PDE Heat Equation')
plt.xlabel('Distance [m]')
plt.ylabel('Temperature [$\degree$ c')
plt.legend([f't = {value} s' for value in t])
plt.grid(color='grey', linestyle=':', linewidth=1.0, axis='x', alpha=0.5)
plt.grid(color='grey', linestyle=':', linewidth=1.0, axis='x=y', alpha=0.5)
plt.show