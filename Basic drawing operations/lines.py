import cairo

#Set up surface
surface= cairo.ImageSurface(cairo.FORMAT_RGB24,600,400)
ctx=cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()


#Draw a line
ctx.move_to(100, 100)
ctx.line_to(500, 300)
ctx.set_source_rgb(0,0,1)
ctx.set_line_width(3)
ctx.stroke()
surface.write_to_png("line.png")