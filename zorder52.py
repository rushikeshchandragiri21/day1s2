
import matplotlib.pyplot as plt

# Convert 2D coordinates to Z-order value
def to_z_order(x, y):
    value = 0
    n = len(x)
    for i in range(n):
        if x[i] == '1':
            value = (value << 1) | 1
        else:
            value = (value << 1) | 0
        if y[i] == '1':
            value = (value << 1) | 1
        else:
            value = (value << 1) | 0
    return value

# Convert decimal value to its binary representation
def get_bits(value, n):
    if value == 0:
        return "0" * n
    bits = ""
    leading_zeros = True
    for i in range(n - 1, -1, -1):
        if (value & (1 << i)) != 0:
            bits += "1"
            leading_zeros = False
        elif not leading_zeros:
            bits += "0"
    return bits

# Generate binary coordinates within a range
def generate_binary_coordinates(n):
    coordinates = []
    for i in range(2 ** n):
        binary = format(i, f'0{n}b')
        coordinates.append(binary)
    return coordinates

# Plot Z-order curve
def plot_z_order_curve(coordinates):
    x = []
    y = []
    for coord in coordinates:
        x_val = int(coord[::2], 2)  # Extract x bits
        y_val = int(coord[1::2], 2)  # Extract y bits
        x_bin = get_bits(x_val, len(coord) // 2)
        y_bin = get_bits(y_val, len(coord) // 2)
        x.append(x_bin)
        y.append(y_bin)
    
    plt.plot(x, y, marker='o', linestyle='-', markersize=5)
    plt.title('Z-order Curve')
    plt.xlabel('X (Binary)')
    plt.ylabel('Y (Binary)')
    plt.grid(True)
    plt.show()

# Check if a point is present on Z-order curve
def contains_point(z_index, x, y):
    z_order = to_z_order(x, y)
    return z_order in z_index

if __name__ == "__main__":
    # Considering 4-bit values
    binary_coordinates = generate_binary_coordinates(4)
    z_index = {}
    for coord in binary_coordinates:
        z_order = to_z_order(coord[:len(coord)//2], coord[len(coord)//2:])
        z_index[z_order] = coord
    
    # Get all points stored
    print("Z-order Points:")
    for key, value in z_index.items():
        print("ZOrder:", value, ", Decimal:", key)

    # Plot Z-order curve
    plot_z_order_curve(z_index.values())

    # Check if a point is present on Z-order curve
    x_to_check = "0101"  # Example x-coordinate to check
    y_to_check = "1010"  # Example y-coordinate to check
    if contains_point(z_index, x_to_check, y_to_check):
        print(f"Point ({x_to_check}, {y_to_check}) is present on the Z-order curve.")
    else:
        print(f"Point ({x_to_check}, {y_to_check}) is not present on the Z-order curve.")
