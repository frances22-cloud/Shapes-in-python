import cairo

# Define the canvas size and background color
canvas_width, canvas_height = 400, 300
background_color = (1.0, 1.0, 1.0)  # White

# Create a Cairo surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas_width, canvas_height)
context = cairo.Context(surface)

# Set the background color
context.set_source_rgb(*background_color)
context.rectangle(0, 0, canvas_width, canvas_height)
context.fill()

# Load and add your image to the canvas
# image_path = "your_image.jpg"  # Replace with the path to your image
# with cairo.ImageSurface.create_from_png(image_path) as img_surface:
#     img_width, img_height = img_surface.get_width(), img_surface.get_height()
#     x = (canvas_width - img_width) / 2
#     y = (canvas_height - img_height) / 2
#     context.set_source_surface(img_surface, x, y)
#     context.paint()

# Save the canvas as an image
output_path = "output_canvas.png"
surface.write_to_png(output_path)

print("Canvas with image saved to", output_path)
