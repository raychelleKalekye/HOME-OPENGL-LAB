import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1000, 1000)
ctx = cairo.Context(surface)


ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# house
line_width = 5
ctx.set_line_width(line_width)

#the walls
ctx.move_to(50, 204)
ctx.line_to(50, 350)
ctx.line_to(180, 350)
ctx.line_to(180, 204)
ctx.move_to(180, 204)
ctx.line_to(180, 350)
ctx.line_to(430, 350)
ctx.line_to(430, 200)
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

