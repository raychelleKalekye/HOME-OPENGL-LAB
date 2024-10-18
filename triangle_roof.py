import cairo


width, height = 1000, 1000
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)


line_width = 5
ctx.set_line_width(line_width)
#triangle roof
ctx.move_to(115, 115)
ctx.line_to(25, 210)
ctx.line_to(36, 220)
ctx.line_to(115, 140)
ctx.line_to(194, 220)
ctx.line_to(203, 210)
ctx.close_path()
ctx.stroke()


surface.write_to_png("house.png")