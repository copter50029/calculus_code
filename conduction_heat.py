import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

L = 1.0
W = 1.0

k = 10 # กราฟยกตัว
Q_dot = 100000

qf = 15
h=100
Tf = 30
TL = 200
TR = 10

nx = 25 #more detail
ny = 25 #more detail
dx = L/(nx-1)
dy = W/(ny-1)

x= np.linspace(0,L,nx)
y= np.linspace(0,W,ny)
X,Y = np.meshgrid(x,y)

T = np.array([[0.0]*nx]*ny)

T[0:,0] = TL
T[0:,-1] = TR

tol = 1e-6
T_old = np.array([[0.0]*nx]*ny)
dT = 1


# Iterations while dT > tol:
# Interior Nodes (East, West, North, South)
while dT > tol:
    aE = aW = k*dy/dx
    aN = aS = k*dx/dy
    aP = aE + aW + aN + aS
    T[1:-1,1:-1] = (aE*T[1:-1,2:] + aW*T[1:-1,0:-2]+\
                    aN*T[2:,1:-1] + aW*T[0:-2,1:-1]+\
                        Q_dot*dx*dy)/aP
    # Bottom Nodes
    aE = aw = 0.5*k*dy/dx
    aN = k*dx/dy
    aP = aE + aW + aN
    T[0,1:-1] = (aE*T[0,2:] + aW*T[-0,0:-2] + aN*T[1,1:-1] + 0.5*Q_dot*dx*dy + qf*dx)/aP
    # Top Nodes
    aE = aW = 0.5*k*dy/dx
    aS =k*dx/dy
    aP = aE + aW + aS + h*dx
    T[-1,1:-1] = (aE*T[-1,2:] + aW*T[-1,0:-2] + aS*T[-2,1:-1]+ 0.5*Q_dot*dx*dy + h*dx*Tf)/aP
    dT = np.max(np.abs(T-T_old))
    T_old[:,:] = T[:,:]
    
plt.scatter(X,Y)
plt.plot(X,Y,c ="k")
plt.plot(np.transpose(X),np.transpose(Y),c="k")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# Contour plot of temperature distribution
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
# Plot the 3D surface of temperature distribution 
surf = ax.plot_surface (X,Y,T,cmap=cm.coolwarm,linewidth=0, antialiased=False) 
plt.title('Temperature distribution (oC)', fontsize=10)
# Projection the surface to the x-y plane 

ax.contourf(X,Y,T,zdir='z',offset=50,cmap='coolwarm')
ax.set_xlabel('x') 
ax.set_ylabel('y')
ax.set_zlabel('Temperature')
# Add a colar bar which maps values to colors. 
fig.colorbar(surf, shrink=0.5, aspect=8)
plt.show()

plt.plot(x,T[int(nx/2),0:],"-o")
plt.grid()
plt.xlabel("x,[m]")
plt.ylabel("Temperature,[$^\circ$C]")
plt.title("Temperature distribution")
plt.show()