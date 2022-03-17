import pygame
import random

pygame.init()
width = 700
heigth = 600
win = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Bomber")
clock= pygame.time.Clock()

time = 0

class player():
  def __init__(self, name, x, img):
    self.name = name
    self.speed = 3
    self.img = pygame.image.load(img)
    self.player = pygame.transform.scale(self.img, (50, 50))
    self.rect = pygame.Rect(x, 300, 50 ,50)
    self.hp = 3
class bomb():
  def __init__(self):
    self.speed = 2
    self.img = pygame.image.load('Images/Player1.png')
    self.bomb = pygame.transform.scale(self.img, (50, 50))
    self.rect = pygame.Rect(random.randint(0, width), -50, 50 ,50)
class speedbomb():
  def __init__(self):
    self.speed = random.randint(3, 6)
    self.img = pygame.image.load('Images/Player1.png')
    self.bomb = pygame.transform.scale(self.img, (50, 50))
    self.rect = pygame.Rect(random.randint(0, width), -100, 50 ,50)

bomblast = 0
bombtime = 700
bombs = [bomb()]
players = [player('blue', 10, 'Images/Player1.png'), player('red', 700, 'Images/Player1.png')]


def p_move(p):
    keys = pygame.key.get_pressed()
    if p.name == "blue":
      if keys[pygame.K_a]:
        if p.rect.x != 0:
          p.rect.x -= p.speed
  
      if keys[pygame.K_d]:
        if p.rect.x != width:
          p.rect.x += p.speed
    else:
      if keys[pygame.K_LEFT]:
        if p.rect.x != 0:
          p.rect.x -= p.speed
  
      if keys[pygame.K_RIGHT]:
        if p.rect.x != width:
          p.rect.x += p.speed     
    win.blit(p.player, (p.rect.x, p.rect.y))

def p_coll (p):
  for b in bombs:
    if p.rect.colliderect(b.rect):
      bombs.remove(b)
      p.hp -= 1
      if p.hp == 0:
        players.remove(p)
      print(p.hp)

def bomb_move(b):
  b.rect.y += b.speed
  win.blit(b.bomb, (b.rect.x, b.rect.y))
  if b.rect.y > 300:
    bombs.remove(b)

def bomb_spawn():
  global bombtime
  global bomblast
  if now - bomblast >= bombtime:
    if 700-10*time > 250:
      bombtime = 700-10*time
    else:
      bombtime = 250
    if random.randint(0, 4) == 0:
      bombs.append(speedbomb())
    else:
      bombs.append(bomb())
    bomblast = pygame.time.get_ticks()

while True:
  now = pygame.time.get_ticks()
  clock.tick(60)
  time = pygame.time.get_ticks()/1000
  win.fill((0, 0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()

#call player functions
  for p in players:
    p_move(p)
    p_coll(p)
    
#movement bombs
  for b in bombs:
    bomb_move(b)

  bomb_spawn()
  pygame.display.update()
  
