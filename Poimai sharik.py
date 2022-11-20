#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
import pygame
from pygame.draw import *
from random import randint
pygame.init()

width = 1200
height = 900
FPS = 30
screen = pygame.display.set_mode((width, height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

figures = []

def risovashka():
    '''
    Рисуем и двигаем фигуру.
    '''
    pass
    for figure in figures:
        figure.draw()
        figure.move()
    
class Ball:
    def __init__(self, x, y, vx, vy, r, color):
        '''
        Обозначаем для круга переменные в классе.
        '''
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
        self.color = color
    def draw(self):
        '''
        Рисуем шарик.
        '''
        circle(screen, self.color, (self.x, self.y), self.r)
    def move(self):
        '''
        Двигаем шарик и смотрим столкновения.
        '''
        self.x += self.vx/FPS
        self.y += self.vy/FPS
        if self.x + self.r >= width or self.x - self.r <= 0:
            self.vx = -self.vx
        if self.y + self.r >= height or self.y - self.r <= 0:
            self.vy = -self.vy
    def is_hit(self, x, y):
        '''
        Проверяем, было ли нажатие на круг.
        '''
        return (x - self.x)**2 + (y - self.y)**2 <= (self.r)**2
    
class Square:
    def __init__(self, x, y, vx, vy, a, color):
        '''
        Обозначаем для квадрата переменные в классе.
        '''
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.a = a
        self.color = color
    def draw(self):
        '''
        Рисуем квадрат.
        '''
        rect(screen, self.color, (self.x - self.a/2, self.y - self.a/2, self.a, self.a))
    def move(self):
        '''
        Двигаем квадрат и смотрим столкновения.
        '''
        self.x += self.vx/FPS
        self.y += self.vy/FPS
        if self.x + self.a/2 >= width or self.x - self.a/2 <= 0:
            self.vx = -self.vx
        if self.y + self.a/2 >= height or self.y - self.a/2 <= 0:
            self.vy = -self.vy
    def is_hit(self, x, y):
        '''
        Проверяем, было ли нажатие на квадрат.
        '''
        return self.x - self.a/2 <= x <= self.x + self.a/2 and self.y - self.a/2 <= y <= self.y + self.a/2

def figurka():
    global summa
    '''
    Смотрим на какую фигуру была мышка нажата: квадрат или круг, и удаляем ее.
    '''
    pass
    i = 0
    while i < len(figures):
        if figures[i].is_hit(event.pos[0], event.pos[1]):
            figures.remove(figures[i])
            summa += 1
            i -= 1
            break
        i += 1
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

summa = 0

for i in range(randint(1,10)):
    figures.append(Ball(randint(100, 500), randint(100, 500), randint(10, 60), randint(10, 60), randint(30, 100), COLORS[randint(0, 5)]))
for i in range(randint(1,10)):
    figures.append(Square(randint(100, 500), randint(100, 500), randint(10, 60), randint(10, 60), randint(30, 100), COLORS[randint(0, 5)]))

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            figurka()
    risovashka()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
print('Количество очков: ', summa)


# In[ ]:




