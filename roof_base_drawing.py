import cairo


width, height = 1000, 1000
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)


#drawing the roof
ctx.set_source_rgb(0,0,0)
ctx.move_to(194,200)
ctx.line_to(117,115)
ctx.line_to(350,115)
ctx.line_to(440,200)
ctx.set_line_width(5)
ctx.close_path()
ctx.stroke()


#drawing the base
ctx.set_source_rgb(0,0,0)
ctx.rectangle(40,350,400,20)
ctx.set_line_width(5)
ctx.stroke()

surface.write_to_png("2D_house.png")