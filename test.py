#!/usr/bin/python2.7
import sys
import pygame
import random
from pygame import *

import richard
import game

pygame.init()

WIN_WIDTH = 1366
WIN_HEIGHT = 768

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

nost = pygame.mixer_music.load("nost.mp3")
swing = pygame.mixer.Sound("swing.wav")

bg = pygame.Surface(DISPLAY)
screen = pygame.display.set_mode(DISPLAY)
clock = pygame.time.Clock()

pygame.mouse.set_visible(True)
pygame.mixer_music.play(0 ,20)
colors = ["#87ceeb", "#010101", "#ff69b4"]
people = pygame.sprite.Group()

ADD = pygame.USEREVENT + 1

PRINT_POINTS = pygame.USEREVENT + 2
pygame.time.set_timer(PRINT_POINTS, 500)
f = pygame.font.SysFont("BulletInYourHead", 50)

SPEEDUP = pygame.USEREVENT + 3
pygame.time.set_timer(SPEEDUP, 2000)

SWITCH = pygame.USEREVENT + 4
pygame.time.set_timer(SWITCH, 200)

def main():
    points = 0
    counter = 0
    PERIOD = 300    
    pygame.time.set_timer(ADD, PERIOD)
    while 1:
        text = f.render("points: {}".format(str(richard.Richard.points)), 1, Color("#ff0000"))                   
        textpos = text.get_rect(centerx=screen.get_width()/2)
        tick = pygame.time.get_ticks()
        clock.tick(60)
         
        if (int(pygame.time.get_ticks()) % 10) == 0:
            random.shuffle(colors)
        next_color = colors[0]
        
        for e in pygame.event.get():
            if e.type == SWITCH:
                for x in people:
                    x.switch()
            if e.type == SPEEDUP:
                if PERIOD > 10:
                    PERIOD -= 50
                    print PERIOD
            if e.type == ADD:
                people.add(richard.Richard())
            if e.type == pygame.QUIT:
                raise SystemExit, "QUIT"
            if e.type == pygame.MOUSEBUTTONDOWN:
                hit_check = len(people)
                for x in people:
                    x.punch(mouse.get_pos())
                if hit_check == len(people):
                    swing.play()
                    richard.Richard.points -= 10
            if e.type == PRINT_POINTS:
                richard.Richard.count_points()
        people.update()
        screen.fill(Color(next_color))
        people.draw(screen)
        screen.blit(text, textpos)
        pygame.display.update() 

if __name__ == "__main__":
    main()
