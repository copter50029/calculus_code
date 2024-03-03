import numpy as np
import matplotlib.pyplot as plt
import math
import csv

theta = float(input('enter angle in degree:'))
u = float(input('enter initial velocity in m/s:'))

def Plotxy(x, y):
    plt.plot(x, y, color='c', linewidth=1.5, label='y=f(x)')
    plt.title('plot of projectile y=f(x)')
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.legend()
    plt.grid(alpha=.4, linestyle='--')
    plt.show()

def Plotyt(y, t):
    plt.plot(t, y, color='b', linewidth=1.5, label='y=f(t)')
    plt.title('plot of vertical vs. time y=f(t)')
    plt.xlabel('t (sec)')
    plt.ylabel('y (m)')
    plt.legend()
    plt.grid(alpha=.4, linestyle='--')
    plt.show()

def Plotxt(x, t):
    plt.plot(t, x, color='m', linewidth=1.5, label='x=f(t)')
    plt.title('plot of horizontal distance vs. time x=f(t)')
    plt.xlabel('t (sec)')
    plt.ylabel('x (m)')
    plt.legend()
    plt.grid(alpha=.4, linestyle='--')
    plt.show()

def CalProjectile(u, theta):
    g = 9.81
    theta_r = np.radians(theta)
    R = (u ** 2) * math.sin(2 * theta_r) / g
    h = (u ** 2) * (math.sin(theta_r)) ** 2 / (2 * g)
    x = np.linspace(0, R, 50)
    y = (x * math.tan(theta_r)) - (1 / 2) * (g * x ** 2) / (u ** 2 * (math.cos(theta_r)) ** 2)
    t = x / (u * math.cos(theta_r))
    T = 2 * u * math.sin(theta_r) / g

    return x, y, t, h, R, T

out = CalProjectile(u, theta)

x = out[0]
y = out[1]
t = out[2]
h = out[3]
R = out[4]
T = out[5]

# Plotting functions...
# ...

# Print and save results to CSV file
csv_filename = f'2320110xxx_out(1).csv'
with open(csv_filename, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['time(sec)', 'distance(m)', 'height(m)'])
    for i in range(len(t)):
        csv_writer.writerow([t[i], x[i], y[i]])

print('maximum height =', round(h, 2), 'm')
print('maximum distance =', round(R, 2), 'm')
print('time spent =', round(T, 2), 'sec')
print(f'Results saved to {csv_filename}')