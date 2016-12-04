import pygame
import random


class Richard(pygame.sprite.Sprite):
    count = 0
    points = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frame1 = pygame.transform.scale(pygame.image.load("richard1.png"), (192, 248))
        self.frame2 = pygame.transform.scale(pygame.image.load("richard2.png"), (192, 248))
        self.image = self.frame2
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.x = random.randint(0, 1000)
        self.rect.y = random.randint(0, 500)
        self.hit = False
        self.smash = pygame.mixer.Sound("punch.wav")
        Richard.count += 1

    @staticmethod
    def count_points():
        if Richard.count > 1:
            Richard.points -= 100
        return Richard.points

    def switch(self):
        if self.image == self.frame2:
            self.image = self.frame1
        elif self.image == self.frame1:
            self.image = self.frame2

    def update(self):
        if self.hit == True:
            Richard.count -= 1
            Richard.points += 50
            self.kill()

    def punch(self, coords):
        if self.rect.collidepoint(coords):
            self.hit = True
            self.smash.play()
