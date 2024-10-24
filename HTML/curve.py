import numpy as np
import math
import matplotlib.pyplot as plt

# Function to compute the binomial coefficient
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Function to compute a single point on the Bezier curve at parameter t
def bezier_point(control_points, t):
    n = len(control_points) - 1
    point = np.zeros(2)
    for i, p in enumerate(control_points):
        bernstein_polynomial = binomial_coefficient(n, i) * (t ** i) * ((1 - t) ** (n - i))
        point += bernstein_polynomial * np.array(p)
    return point

# Function to compute all points on the Bezier curve
def bezier_curve(control_points, num_points=100):
    curve = []
    for t in np.linspace(0, 1, num_points):
        curve.append(bezier_point(control_points, t))
    return np.array(curve)

# Function to plot the control points and the Bezier curve
def plot_bezier_curve(control_points, curve):
    control_points = np.array(control_points)
    
    # Plot control points and polygon
    plt.plot(control_points[:, 0], control_points[:, 1], 'ro--', label='Control Points')
    
    # Plot Bezier curve
    plt.plot(curve[:, 0], curve[:, 1], 'b-', label='Bezier Curve')

    # Labeling and showing the plot
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function to get user input and compute the Bezier curve
def main():
    n = int(input("Enter the number of control points: "))
    control_points = []
    for i in range(n):
        x, y = map(float, input(f"Enter control point {i + 1} (x, y): ").split())
        control_points.append((x, y))

    curve = bezier_curve(control_points)
    plot_bezier_curve(control_points, curve)

if __name__ == "__main__":
    main()
