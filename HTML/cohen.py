import matplotlib.pyplot as plt

# Define region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Window boundaries
x_min, y_min = 50, 50
x_max, y_max = 150, 150

# Function to compute region code
def compute_code(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code

# Cohen-Sutherland line clipping algorithm
def cohen_sutherland_clip(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2 != 0:
            break
        else:
            x, y = 0.0, 0.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        return [(x1, y1), (x2, y2)]
    else:
        return None

# Function to draw the clipping window
def draw_clipping_window():
    plt.plot([x_min, x_max], [y_min, y_min], color='black')
    plt.plot([x_max, x_max], [y_min, y_max], color='black')
    plt.plot([x_max, x_min], [y_max, y_max], color='black')
    plt.plot([x_min, x_min], [y_max, y_min], color='black')

# Main function to input and process lines
def main():
    # Input line coordinates
    x1, y1 = map(int, input("Enter the starting point (x1, y1): ").split())
    x2, y2 = map(int, input("Enter the ending point (x2, y2): ").split())

    # Draw the clipping window
    draw_clipping_window()

    # Plot the original line
    plt.plot([x1, x2], [y1, y2], color='blue', label='Original Line')

    # Perform line clipping
    clipped_line = cohen_sutherland_clip(x1, y1, x2, y2)

    if clipped_line:
        x_clipped, y_clipped = zip(*clipped_line)
        plt.plot(x_clipped, y_clipped, color='red', label='Clipped Line')
        plt.legend()
    else:
        print("Line is outside and cannot be clipped.")
    
    # Show the plot
    plt.xlim(0, 200)
    plt.ylim(0, 200)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
