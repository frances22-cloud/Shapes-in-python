import cairo
import math

# Set up pycairo
surface = cairo.ImageSurface (cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)

# Small Circle
ctx.arc(300, 200, 50, 0, 2*math.pi)
ctx.set_source_rgb(1, 0, 0)
ctx.paint()
ctx.set_line_width(10)
ctx.stroke()

# Medium Circle
ctx.arc(300, 200, 100, 0, 2*math.pi)
ctx.set_source_rgb(1, 0, 1)
ctx.set_line_width(10)
ctx.stroke()

# Large Circle
ctx.arc(300, 200, 150, 0, 2*math.pi)
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(10)
ctx.stroke()

#Displaying the circle
surface.write_to_png("Basic drawing operations/circle.png")