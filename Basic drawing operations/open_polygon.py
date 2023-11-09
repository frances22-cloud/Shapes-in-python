import cairo

#Set up surface
surface= cairo.ImageSurface(cairo.FORMAT_RGB24,600,400)
ctx=cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()


#Open polygon
ctx.move_to(50, 200) #A
ctx.line_to(100, 200) #B
ctx.line_to(150,250) #C
ctx.line_to(250, 150) #D
ctx.line_to(350, 250)
ctx.line_to(450, 150)
ctx.line_to(500, 200)
ctx.line_to(550, 200)
ctx.set_source_rgb(1,1,0)
ctx.set_line_width(10)
ctx.stroke()

#displaying the canvas
surface.write_to_png("open_polygon.png")