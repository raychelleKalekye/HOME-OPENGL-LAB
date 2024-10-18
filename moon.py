import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1000, 1000)
ctx = cairo.Context(surface)


ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Moon
moon_center_x = 900
moon_center_y = 100
moon_radius = 100


ctx.set_source_rgb(0.5, 0.5, 0.5)
ctx.arc(moon_center_x, moon_center_y, moon_radius, 0, 2 * math.pi)
ctx.fill()


ctx.set_source_rgb(1.0, 1.0, 1.0)
ctx.arc(moon_center_x - 40, moon_center_y, moon_radius, 0, 2 * math.pi)
ctx.fill()


surface.write_to_png("house_with_moon.png")
print("moon")
