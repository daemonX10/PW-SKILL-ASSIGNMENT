import numpy as np
import matplotlib.pyplot as plt

# Plot the polygon and apply transformation
def plot_polygon(points, transformed_points=None):
    fig, ax = plt.subplots()
    # Original polygon
    x, y = zip(*points)
    ax.plot(x + (x[0],), y + (y[0],), label="Original", color="blue")
    
    # Transformed polygon if exists
    if transformed_points is not None:
        tx, ty = zip(*transformed_points)
        ax.plot(tx + (tx[0],), ty + (ty[0],), label="Transformed", color="red")
    
    ax.set_aspect('equal')
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.legend()
    plt.grid(True)
    plt.show()

# Reflection with respect to X-axis
def reflect_x(points):
    transformation_matrix = np.array([[1, 0, 0],
                                      [0, -1, 0],
                                      [0, 0, 1]])
    return apply_transformation(points, transformation_matrix)

# Reflection with respect to Y-axis
def reflect_y(points):
    transformation_matrix = np.array([[-1, 0, 0],
                                      [0, 1, 0],
                                      [0, 0, 1]])
    return apply_transformation(points, transformation_matrix)

# Shearing function
def shear(points, shx, shy):
    transformation_matrix = np.array([[1, shx, 0],
                                      [shy, 1, 0],
                                      [0, 0, 1]])
    return apply_transformation(points, transformation_matrix)

# Apply transformation matrix to points
def apply_transformation(points, matrix):
    transformed_points = []
    for point in points:
        x, y = point
        original_vector = np.array([x, y, 1])
        transformed_vector = np.dot(matrix, original_vector)
        transformed_points.append(transformed_vector[:2])  # Only x, y coordinates
    return transformed_points

# Function to get user-defined polygon
def get_polygon():
    n = int(input("Enter number of vertices for the polygon: "))
    points = []
    print("Enter the coordinates of the vertices (x, y):")
    for i in range(n):
        x, y = map(float, input(f"Vertex {i + 1}: ").split())
        points.append((x, y))
    return points

# Main menu-driven function
def main():
    points = get_polygon()  # Get user-defined polygon

    while True:
        print("\n1. Reflect with respect to X-axis")
        print("2. Reflect with respect to Y-axis")
        print("3. Shearing")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            transformed_points = reflect_x(points)
            plot_polygon(points, transformed_points)
        elif choice == 2:
            transformed_points = reflect_y(points)
            plot_polygon(points, transformed_points)
        elif choice == 3:
            shx = float(input("Enter shear factor along X: "))
            shy = float(input("Enter shear factor along Y: "))
            transformed_points = shear(points, shx, shy)
            plot_polygon(points, transformed_points)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
