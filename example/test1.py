#!/usr/bin/python2.7
import pygame

import sys

STEP = 10
G = 1
x = 100
y = 100
vy = 0

screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
red = pygame.Color("red")


def main():
    while True:
        global x, vy
        vy -= G
        x -= 1
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                move(e)
            else:
                pygame.draw.rect(screen, pygame.Color("black"),
                                 pygame.Rect(0, 0, screen.get_width(), screen.get_height()))
                pygame.draw.rect(screen, red, pygame.Rect(x, y, 50, 50))
                pygame.display.flip()


def move(e):
    global x, y, screen, STEP
    if e.key == pygame.K_LEFT and x >= STEP:
        x -= STEP
    elif e.key == pygame.K_RIGHT and x <= screen.get_width() - STEP:
        x += STEP
    elif e.key == pygame.K_UP and y >= STEP:
        y -= STEP
    elif e.key == pygame.K_DOWN and y <= screen.get_height() - STEP:
        y += STEP


if __name__ == '__main__':
    main()
