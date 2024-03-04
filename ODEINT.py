import numpy as np
import matplotlib.pyplot as plt

nx, ny = 0.5, 0.5

x_1 = np.arange(-3, 3, nx)
y_1 = np.arange(-3, 3, ny)

x_2 = np.arange(-3, 3, nx)
y_2 = np.arange(-3, 3, ny)

x_3 = np.arange(-3, 3, nx)
y_3 = np.arange(-3, 3, ny)

x_4 = np.arange(-3, 3, nx)
y_4 = np.arange(-3, 3, ny)

x_5 = np.arange(-3, 3, nx)
y_5 = np.arange(-3, 3, ny)

x_6 = np.arange(-3, 3, nx)
y_6 = np.arange(-3, 3, ny)

# q1
x1, y1 = np.meshgrid(x_1, y_1)
dy = 1 / x1
dx = np.ones(dy.shape)
plt.subplot(2, 3, 1)
plt.xlabel('x')
plt.ylabel('y1')
plt.quiver(x1, y1, dx, dy, color='blue')
plt.title('y\'(x) = f(x) = 1/x')

# q2
x2, y2 = np.meshgrid(x_2, y_2)
dy = 1 / y2
dx = np.ones(dy.shape)
plt.subplot(2, 3, 2)
plt.xlabel('x2')
plt.ylabel('y2')
plt.quiver(x2, y2, dx, dy, color='red')
plt.title('y\'(x) = f(y) = 1/y')

# q3
x3, y3 = np.meshgrid(x_3, y_3)
dy = np.exp(-x3**2)
dx = np.ones(dy.shape)
plt.subplot(2, 3, 3)
plt.xlabel('x3')
plt.ylabel('y3')
plt.quiver(x3, y3, dx, dy, color='green')
plt.title('y\'(x) = f(x) = exp(-x^2)')

# q4
x4, y4 = np.meshgrid(x_4, y_4)
dy = y4**2 - 1
dx = np.ones(dy.shape)
plt.subplot(2, 3, 4)
plt.xlabel('x4')
plt.ylabel('y4')
plt.quiver(x4, y4, dx, dy, color='cyan')
plt.title('y\'(x) = f(y) = y^2 - 1')

# q5
x5, y5 = np.meshgrid(x_5, y_5)
dy = (x5 + y5) / (x5 - y5)
dx = np.ones(dy.shape)
plt.subplot(2, 3, 5)
plt.xlabel('x5')
plt.ylabel('y5')
plt.quiver(x5, y5, dx, dy, color='cyan')
plt.title('y\'(x) = f(y) = (x+y)/(x-y)')

# q6
x6, y6 = np.meshgrid(x_6, y_6)
dy = np.sin(x6) * np.sin(y6)
dx = np.ones(dy.shape)
plt.subplot(2, 3, 6)
plt.xlabel('x6')
plt.ylabel('y6')
plt.quiver(x6, y6, dx, dy, color='black')
plt.title('y\'(x) = f(y) = sin(x)*sin(y)')

plt.tight_layout()
plt.show()