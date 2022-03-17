import pygame
from random import randint

pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bomber")
clock= pygame.time.Clock()

bombs = []

speed = 1
player1_img = pygame.image.load('Images/Player1.png')
player1 = pygame.transform.scale(player1_img, (50, 50))
p1 = pygame.Rect(10, 300, 50 ,50)

def draw(p1):
  win.fill((0, 0, 0))
  win.blit(player1, (p1.x, p1.y))
  pygame.display.update()

def p1_move():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        p1.x -= speed

    if keys[pygame.K_RIGHT]:
        p1.x += speed

  
while True:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()

#movement player
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_LEFT]:
      p1.x -= speed

  if keys[pygame.K_RIGHT]:
      p1.x += speed

#movement bombs
  for bomb in bombs:
    print("")
  p1_move()
  draw(p1)
  
