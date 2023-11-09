import cairo

# Create a new Cairo surface (here, we create an image surface)
width, height = 400, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

# Set line width and color
ctx.set_line_width(6)
ctx.set_source_rgb(1, 0, 1)  # Black color (RGB values)

# Function to draw a square
def draw_square(x, y, side_length):
    ctx.rectangle(x, y, side_length, side_length)
    ctx.stroke()

# Function to draw a circle
def draw_circle(x, y, radius):
    ctx.arc(x, y, radius, 0, 2 * 3.14159265359)
    ctx.stroke()

# Function to save the drawing to an image file
def save_image(filename):
    surface.write_to_png(filename)

# Call the functions to draw shapes
draw_square(100, 100, 100)
draw_circle(200, 200, 50)

# Save the drawing to an image file
save_image("shapes.png")



