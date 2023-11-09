import cairo
import math

# Set up surface
surface = cairo.ImageSurface (cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)

r = 200
x1 = 300
y1 = 200
# Relative drawing function
a = 0.523599 # 0.523599 radian equals 30 degree
ctx.move_to(x1, y1)
ctx.line_to(x1 + r*math.cos(a), y1 + r*math.sin(a))
ctx.stroke()

#displaying the canvas
surface.write_to_png("ComplexLines.png")