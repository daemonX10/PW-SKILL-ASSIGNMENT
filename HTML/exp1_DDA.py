import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc, y_inc = dx / steps, dy / steps
    x, y = x1, y1
    x_points, y_points = [], []
    
    for _ in range(steps+1):
        x_points.append(x)
        y_points.append(y)
        x += x_inc
        y += y_inc

    plt.plot(x_points, y_points)
    plt.show()

x1, y1 = map(int, input("Enter x1, y1 for DDA: ").split())
x2, y2 = map(int, input("Enter x2, y2 for DDA: ").split())
DDA(x1, y1, x2, y2)
