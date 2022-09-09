from turtle import width
import pygame
import math
import colorsys
pygame.init()

white = (255, 255, 255)
black = (0,0,0)
hue = 0

width = 1920
height = 1080

x_start, y_start = 0, 0

x_seperator = 10
y_seperator = 20

rows = height//y_seperator
columns = width//x_seperator
screen_size = rows*columns

x_offset = columns/2
y_offset = rows/2

A,B =0, 0 

theta_spacing = 10
phi_spacing = 1

chars = ".,-~:;=!*#$@"

screen = pygame.display.set_mode((width, height))

display_surface = pygame.display.set_mode((width, height))

pygame.display.set_caption('Donut')
font = pygame.font.SysFont('Arial', 18, bold=True)

def hsv2rgb(h, s, v):
    return tuple(round(i*255)for i in colorsys.hsv_to_rgb(h, s, v))

#def text_display(letter, x_start, y_start):
#    text = font.render(str(letter), True, white)
#    display_surface.blit(text, (x_start, y_start))

def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, hsv2rgb(hue, 1, 1))
    display_surface.blit(text, (x_start, y_start))

run = True
while run:
    screen.fill((black))

    z = [0] * screen_size
    w = [' '] * screen_size

    for j in range(0, 628, theta_spacing):  # from 0 to 2pi
        for i in range(0, 628, phi_spacing):  # from 0 to 2pi
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))  # 3D x coordinate after rotation
            y = int(y_offset + 20 * D * (l * h * n + t * m))  # 3D y coordinate after rotation
            o = int(x + columns * y)  
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))  # luminance index
            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                w[o] = chars[N if N > 0 else 0]

    if y_start == rows * y_seperator - y_seperator:
        y_start = 0

    for i in range(len(w)):
        A += 0.000008  # for faster rotation change to bigger value
        B += 0.000006  # for faster rotation change to bigger value
        if i == 0 or i % columns:
            text_display(w[i], x_start, y_start)
            x_start += x_seperator
        else:
            y_start += y_seperator
            x_start = 0
            text_display(w[i], x_start, y_start)
            x_start += x_seperator

    pygame.display.update()

    hue += 0.005

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False