import matplotlib.pyplot as plt
import numpy as np

# Set up the grid and colors
grid_size = 100
grid = np.ones((grid_size, grid_size, 3))  # RGB grid, initially white
boundary_color = [0, 0, 0]  # Black boundary
fill_color = [1, 0, 0]  # Red color
original_color = [1, 1, 1]  # White background

# Boundary Fill 4-connected
def boundary_fill_4(x, y):
    if not (0 <= x < grid_size and 0 <= y < grid_size):
        return
    if (grid[x, y] == boundary_color).all() or (grid[x, y] == fill_color).all():
        return
    
    grid[x, y] = fill_color
    
    boundary_fill_4(x + 1, y)
    boundary_fill_4(x - 1, y)
    boundary_fill_4(x, y + 1)
    boundary_fill_4(x, y - 1)

# Boundary Fill 8-connected
def boundary_fill_8(x, y):
    if not (0 <= x < grid_size and 0 <= y < grid_size):
        return
    if (grid[x, y] == boundary_color).all() or (grid[x, y] == fill_color).all():
        return
    
    grid[x, y] = fill_color
    
    boundary_fill_8(x + 1, y)
    boundary_fill_8(x - 1, y)
    boundary_fill_8(x, y + 1)
    boundary_fill_8(x, y - 1)
    boundary_fill_8(x + 1, y + 1)
    boundary_fill_8(x - 1, y - 1)
    boundary_fill_8(x - 1, y + 1)
    boundary_fill_8(x + 1, y - 1)

# Flood Fill 4-connected
def flood_fill_4(x, y, old_color, new_color):
    if not (0 <= x < grid_size and 0 <= y < grid_size):
        return
    if not (grid[x, y] == old_color).all():
        return
    
    grid[x, y] = new_color
    
    flood_fill_4(x + 1, y, old_color, new_color)
    flood_fill_4(x - 1, y, old_color, new_color)
    flood_fill_4(x, y + 1, old_color, new_color)
    flood_fill_4(x, y - 1, old_color, new_color)

# Flood Fill 8-connected
def flood_fill_8(x, y, old_color, new_color):
    if not (0 <= x < grid_size and 0 <= y < grid_size):
        return
    if not (grid[x, y] == old_color).all():
        return
    
    grid[x, y] = new_color
    
    flood_fill_8(x + 1, y, old_color, new_color)
    flood_fill_8(x - 1, y, old_color, new_color)
    flood_fill_8(x, y + 1, old_color, new_color)
    flood_fill_8(x, y - 1, old_color, new_color)
    flood_fill_8(x + 1, y + 1, old_color, new_color)
    flood_fill_8(x - 1, y - 1, old_color, new_color)
    flood_fill_8(x - 1, y + 1, old_color, new_color)
    flood_fill_8(x + 1, y - 1, old_color, new_color)

# Example boundary (square)
def draw_boundary():
    grid[30:70, 30] = boundary_color
    grid[30:70, 70] = boundary_color
    grid[30, 30:71] = boundary_color
    grid[70, 30:71] = boundary_color

# Main Function
def main():
    global grid
    draw_boundary()

    print("Choose the algorithm:")
    print("1. Boundary Fill 4-connected")
    print("2. Boundary Fill 8-connected")
    print("3. Flood Fill 4-connected")
    print("4. Flood Fill 8-connected")
    
    choice = int(input("Enter your choice (1-4): "))
    
    # Reset grid to original color
    grid = np.ones((grid_size, grid_size, 3))  
    draw_boundary()

    x_start, y_start = map(int, input("Enter starting point (x, y): ").split())
    
    if choice == 1:
        boundary_fill_4(x_start, y_start)
    elif choice == 2:
        boundary_fill_8(x_start, y_start)
    elif choice == 3:
        flood_fill_4(x_start, y_start, original_color, fill_color)
    elif choice == 4:
        flood_fill_8(x_start, y_start, original_color, fill_color)
    else:
        print("Invalid choice!")

    # Plotting the result
    plt.imshow(grid)
    plt.show()

if __name__ == "__main__":
    main()
