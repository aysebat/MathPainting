from canvas import Canvas
from shapes import Square, Rectangle

# Make a dictioney for the color
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "magenta": (255, 0, 255),
    "cyan": (0, 255, 255),
    "black": (0, 0, 0),
    "white": (255, 255, 255)
}

print("An app that lets the user provide the canvas with and desired width and height, and also "
      "start coordinates of geometrical shapes such as squares and rectangles, their dimensions, "
      "and their colors, and the program produces an image file canvas with all the geometrical shapes "
      "drawn in it.")
canvas_width = int(input("Enter the canvas width: "))
canvas_height = int(input("Enter the canvas height: "))
print("------ Color Palette: red, green, blue, yellow, magenta, cyan, black, white ------")
canvas_color = input("Enter canvas color: ")

# Create the canvas with the user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    print("What would you like to drawn? ")
    print(" s : Square")
    print(" r : Rectangle")
    print(" q : Quit the program")
    shape_type = input("Enter the value (s,r,q) : ")

    # Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == "r":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("enter the width of the rectangle: "))
        rec_height = int(input("enter the height of the rectangle: "))
        red = input("The color of rectangle, enter the red value: ")
        green = input("The color of rectangle, enter the green value: ")
        blue = input("The color of rectangle, enter the blue value: ")

        # create the rectangle
        rectangle = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        rectangle.draw(canvas)

    if shape_type.lower() == 's':
        sqr_x = int(input("Enter x of the square: "))
        sqr_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter the side length of the square: "))

        red = input("The color of square, enter the red value: ")
        green = input("The color of square, enter the green value: ")
        blue = input("The color of square, enter the blue value: ")

        #Create the square
        square = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        square.draw(canvas)

    if shape_type == "q":
        break


canvas.make("canvas.png")
