import matplotlib.pyplot as plt

def draw_circle_points_fast(x_center, y_center, x, y, x_points, y_points):
    points = [
        (x_center + x, y_center + y), (x_center - x, y_center + y),
        (x_center + x, y_center - y), (x_center - x, y_center - y),
        (x_center + y, y_center + x), (x_center - y, y_center + x),
        (x_center + y, y_center - x), (x_center - y, y_center - x)
    ]
    for px, py in points:
        x_points.append(px)
        y_points.append(py)

def midpoint_circle_fast(x_center, y_center, radius):
    x_points, y_points = [], []
    x, y = 0, radius
    d = 1 - radius
    draw_circle_points_fast(x_center, y_center, x, y, x_points, y_points)
    
    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        draw_circle_points_fast(x_center, y_center, x, y, x_points, y_points)
    
    return x_points, y_points

x_center, y_center = map(int, input("Enter center coordinates (x, y): ").split())
radius = int(input("Enter the radius of the circle: "))

x_points, y_points = midpoint_circle_fast(x_center, y_center, radius)

plt.scatter(x_points, y_points, s=10, c='b')

# Set the aspect ratio to 'equal' to ensure the circle isn't distorted
plt.gca().set_aspect('equal')

# Add grid and axes for the 4-quadrant system
plt.axhline(0, color='black',linewidth=1)  # X-axis
plt.axvline(0, color='black',linewidth=1)  # Y-axis

# Set limits to show all quadrants
plt.xlim(x_center - radius - 10, x_center + radius + 10)
plt.ylim(y_center - radius - 10, y_center + radius + 10)

plt.grid(True)
plt.show()
