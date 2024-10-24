import matplotlib.pyplot as plt

# Window boundaries
x_min, y_min = 50, 50
x_max, y_max = 150, 150

# Function to check if the point is inside the clipping boundary
def inside(point, edge):
    x, y = point
    if edge == "LEFT":
        return x >= x_min
    elif edge == "RIGHT":
        return x <= x_max
    elif edge == "BOTTOM":
        return y >= y_min
    elif edge == "TOP":
        return y <= y_max

# Function to compute intersection point
def compute_intersection(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2
    if edge == "LEFT":
        x = x_min
        y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
    elif edge == "RIGHT":
        x = x_max
        y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
    elif edge == "BOTTOM":
        y = y_min
        x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
    elif edge == "TOP":
        y = y_max
        x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
    return (x, y)

# Sutherland-Hodgman Polygon Clipping
def sutherland_hodgman_clip(polygon):
    clipped_polygon = polygon
    for edge in ["LEFT", "RIGHT", "BOTTOM", "TOP"]:
        new_polygon = []
        for i in range(len(clipped_polygon)):
            current_point = clipped_polygon[i]
            previous_point = clipped_polygon[i - 1]
            if inside(current_point, edge):
                if inside(previous_point, edge):
                    new_polygon.append(current_point)
                else:
                    new_polygon.append(compute_intersection(previous_point, current_point, edge))
                    new_polygon.append(current_point)
            elif inside(previous_point, edge):
                new_polygon.append(compute_intersection(previous_point, current_point, edge))
        clipped_polygon = new_polygon
    return clipped_polygon

# Plot the original and clipped polygon
def plot_polygons(polygon, clipped_polygon):
    fig, ax = plt.subplots()

    # Plot the clipping window
    ax.plot([x_min, x_max], [y_min, y_min], color='black')
    ax.plot([x_max, x_max], [y_min, y_max], color='black')
    ax.plot([x_max, x_min], [y_max, y_max], color='black')
    ax.plot([x_min, x_min], [y_max, y_min], color='black')

    # Plot the original polygon
    x, y = zip(*polygon)
    ax.plot(x + (x[0],), y + (y[0],), label="Original Polygon", color="blue")

    # Plot the clipped polygon
    if clipped_polygon:
        cx, cy = zip(*clipped_polygon)
        ax.plot(cx + (cx[0],), cy + (cy[0],), label="Clipped Polygon", color="red")
    else:
        print("Polygon completely outside the clipping window.")
    
    ax.set_aspect('equal')
    plt.grid(True)
    plt.legend()
    plt.show()

# Get user-defined polygon
def get_polygon():
    n = int(input("Enter number of vertices for the polygon: "))
    polygon = []
    print("Enter the coordinates of the vertices (x, y):")
    for i in range(n):
        x, y = map(float, input(f"Vertex {i + 1}: ").split())
        polygon.append((x, y))
    return polygon

# Main function
def main():
    polygon = get_polygon()

    # Clipping the polygon
    clipped_polygon = sutherland_hodgman_clip(polygon)

    # Plotting the polygons
    plot_polygons(polygon, clipped_polygon)

if __name__ == "__main__":
    main()

