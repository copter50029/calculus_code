print('Simulation and Plots of 3 Forces balancing')
print('based on DGE-108 Fundamental Physics example 2 modified')
print('-------------------------------------------------------')

import numpy as np
import matplotlib.pyplot as plt
import math

def PlotVector(x1,y1,u1,v1,x2,y2,u2,v2,x3,y3,u3,v3):  
    # Creating plot
    plt.quiver(x1, y1, u1, v1, color='b', units='xy', scale=1)
    plt.quiver(x2, y2, u2, v2, color='m', units='xy', scale=1)
    plt.quiver(x3, y3, u3, v3, color='r', units='xy', scale=1)
    plt.title('Single Vector')
 
    # x-lim and y-lim
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)
 
    # Show plot with grid
    plt.grid()
    plt.show()

def FBD2(i,F1,F2,F3,a1,a2,a3):
    F1x = F1*np.cos(np.radians(a1))
    F1y = F1*np.sin(np.radians(a1))
    F2x = F2*np.cos(np.radians(a2))
    F2y = F2*np.sin(np.radians(a2))
    F3x = F3*np.cos(np.radians(a3))
    F3y = F3*np.sin(np.radians(a3))
   
    PlotVector(0,0,F1x,F1y,0,0,F2x,F2y,0,0,F3x,F3y)
   
    Fx_net = round(F1x + F2x + F3x,2)
    Fy_net = round(F1y + F2y + F3y,2)    
   
    F_net = round(math.sqrt(Fx_net**2 + Fy_net**2),2)
    a4 = round(np.degrees(np.arctan(Fy_net/Fx_net)),2)
   
    F4.append(F_net)
    Theta4.append(a4)
   
    print('Output:',i+1)
    print('F_net_vector =','(',-Fx_net,'.i)','+','(',-Fy_net,'.j)')
    print('F_net_Magnitude = ',F_net,'N')
    print('Direction ceta_r = ',a4,'degrees')
    print('------------------------------------------------------')
   
    return (F4,Theta4)

# Variation of input forces and angles for 2 hours (10-min interval)
F1 =[30,30,25,25,20,20,15,15,20,20,25,25]
F2 = [30,31,32,33,34,35,34,33,32,31,30,29]
F3 = [10,10,10,20,20,20,25,25,25,20,20,20]
a1 = [20,20,20,15,15,15,10,10,10,5,5,5]
a2 = [0,0,0,5,5,5,10,10,10,15,15,15]
a3 = [90,90,90,85,85,85,80,80,80,75,75,75]

# Define output lists
F4 = []
Theta4 = []

# Main program to call function 'FBD2'
for i in range(12):
    FBD2(i,F1[i],F2[i],F3[i],a1[i],a2[i],a3[i])

# Print tabulated from of simulated results    
print('==============================')
print('No    F_net(N)  Angle(Degrees)')  
print('------------------------------')  
for j in range(12):
    print(j+1,'    ', F4[j],'    ',Theta4[j])