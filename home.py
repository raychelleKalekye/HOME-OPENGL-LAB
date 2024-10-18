import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1000, 1000)
ctx = cairo.Context(surface)


ctx.set_source_rgb(1, 1, 1)
ctx.paint()
moon_center_x = 900
moon_center_y = 100
moon_radius = 100


ctx.set_source_rgb(0.5, 0.5, 0.5)
ctx.arc(moon_center_x, moon_center_y, moon_radius, 0, 2 * math.pi)
ctx.fill()


ctx.set_source_rgb(1.0, 1.0, 1.0)
ctx.arc(moon_center_x - 40, moon_center_y, moon_radius, 0, 2 * math.pi)
ctx.fill()
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

# Function to draw a rectangle outline
def draw_rectangle_outline(ctx, x, y, w, h):
    ctx.rectangle(x, y, w, h)
    ctx.set_source_rgb(0, 0, 0)  # Set color to black
    ctx.stroke()

# Function to draw a window sill outline
def draw_window_sill_outline(ctx, x, y, w, h, extension):
    ctx.rectangle(x - extension, y + h , w + 2 * extension, 10)  # Extend sill on both sides
    ctx.set_source_rgb(0, 0, 0)  # Set color to black
    ctx.stroke()


# window 1
window_width = 100  
window_height = 50  
draw_rectangle_outline(ctx, 65, 265, window_width, window_height)  
draw_window_sill_outline(ctx, 65, 265, window_width, window_height, 7)  # Extend sill by 20 pixels on each side

#attic window 
draw_rectangle_outline(ctx, 95, 190, 40, 30) 

# window 2
draw_rectangle_outline(ctx, 255, 265, window_width, window_height) 
draw_window_sill_outline(ctx, 255, 265, window_width, window_height, 7)  # Extend sill by 20 pixels on each side

surface.write_to_png("house_with_moon.png")

