#!/usr/bin/python2.7
import pygame

import sys

STEP = 50
JUMP_V = 24
THRUST_X = 30
MAX_SPEED_X = 30
FRICTION = 1

G = 0.5
x = 100
y = 100
vy = 0
vx = 0

screen = pygame.display.set_mode((1000, 700), pygame.RESIZABLE)
red = pygame.Color("red")


def main():
    while True:
        global x, y, vx, vy
        vy = recalc_vy(y, vy)
        y = recalc_y(y, vy)
        vx = recalc_vx(vx)
        x = recalc_x(x, vx)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                move(e)

        pygame.draw.rect(screen, pygame.Color("black"),
                                 pygame.Rect(0, 0, screen.get_width(), screen.get_height()))
        pygame.draw.rect(screen, red, pygame.Rect(x, y, 50, 50))
        pygame.display.flip()

def recalc_x(x, v):
    if x + v <= 0:
        return 0
    elif x + v >= (screen.get_width() - 50):
        return screen.get_width() - 50
    else:
        return x + v

def recalc_vx(vx):
    if abs(vx) < FRICTION:
        return 0
    elif vx > 0:
        return vx - FRICTION
    else:
        return vx + FRICTION

def recalc_vy(y, v):
    if y >= screen.get_height() - 50 and v <= 0:
        return 0
    # elif y >= screen.get_height() - 50 and v > 0:
    #     return v
    else:
        return v - G

def recalc_y(y, v):
    if (y - v) < 50:
        return 0
    elif (y - v) > screen.get_height() - 50:
        return screen.get_height() - 50
    else:
        return y - v

def move(e):
    global x, y, vx, vy, G
    if e.key == pygame.K_LEFT:
        vx -= THRUST_X
        if vx < -MAX_SPEED_X:
            vx = -MAX_SPEED_X
    elif e.key == pygame.K_RIGHT:
        vx += THRUST_X
        if vx > MAX_SPEED_X:
            vx = MAX_SPEED_X
    elif e.key == pygame.K_UP and (y == screen.get_height() - 50):
        vy += JUMP_V


if __name__ == '__main__':
    main()
