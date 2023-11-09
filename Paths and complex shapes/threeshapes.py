import cairo
# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Red Rectangle
ctx.rectangle(150, 100, 100, 240)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()


# Green Rectangle
ctx. rectangle(300, 100, 100, 240)
ctx.set_source_rgb(0, 1, 0)
ctx.fill()

# Blue Square
ctx.rectangle(350, 170, 200, 200)
ctx.set_source_rgb(0, 0, 1)
ctx.fill()

#Display the surface
surface.write_to_png("threeshapes.png")