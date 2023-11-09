import cairo

#Set up surface
surface= cairo.ImageSurface(cairo.FORMAT_RGB24,600,400)
ctx=cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

#Draw the image
ctx.rectangle(150,100,100,240)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

#Green rectangle
ctx.rectangle(300,100,100,240)
ctx.set_source_rgb(0,1,0)
ctx.fill()

#Blue square
ctx.rectangle(400, 170,200,200)
ctx.set_source_rgb(0, 0,1)
ctx.fill()

surface.write_to_png("rectangle.png")