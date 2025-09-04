def print_rectangular_with_blank(height, width):
    # Check if dimensions are sufficient for a blank center
    if height < 3 or width < 3:
        print("Height and Width must be at least 3 for a blank center.")
        return

    # Create the rectangle
    for row in range(height):
        if row == 0 or row == height - 1:
            # Print the top or bottom row fully filled
            print('*' * width)
        else:
            # Print the rows with blanks in the center
            if width > 2:
                print('*' + ' ' * (width - 2) + '*')

                #* + n blank +*
            else:
                print('*')

#width = j , i = row = height , print for j ,... = *width

# Example usage:
height = 5
width = 9
print_rectangular_with_blank(height, width)
