# Simple Python script to calculate the area of a rectangle

def calculate_area(length, width):
    return length * width

def main():
    print("Welcome to the Area Calculator!")
    
    # Get user input
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    # Calculate the area
    area = calculate_area(length, width)
    
    # Display the result
    print(f"The area of the rectangle is: {area} square units")

if __name__ == "__main__":
    main()
