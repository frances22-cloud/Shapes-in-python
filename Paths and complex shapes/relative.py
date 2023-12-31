import cairo
import math

# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
# Relative drawing function
a = 0.523599 # 0.523599 radian equals 30 degree
r = 200
ctx.move_to(300, 200)
ctx.rel_line_to(r*math.cos(a), r*math.sin(a))
ctx.stroke()

#Displaying the surface
surface.write_to_png("Paths and complex shapes/relative.png")