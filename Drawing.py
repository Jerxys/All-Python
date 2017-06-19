import pygame

pygame.init()

clock = pygame.time.Clock()

size=[500, 500]
surface = pygame.display.set_mode(size)

WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0, 255, 0)
BLUE=(0,0,255)
BLACK=(0,0,0)

dead=False
surface.fill(WHITE)

#Colors specific to home
BOTTOM=(51, 252, 40)
TREE_BOTTOM=(153,89,49)
LEAFS=(57,138,30)
BASE=(189,203,240)

while(dead==False):
 for event in pygame.event.get(): 
  if event.type == pygame.QUIT:
   dead = True
   
  surface.fill(WHITE)
  
  #Draw bottom
  pygame.draw.rect(surface, BOTTOM, [0, 380, 500, 120], 0)
  
  #Draw trees
  pygame.draw.rect(surface, TREE_BOTTOM, [50, 280, 30, 100], 0)
  pygame.draw.rect(surface, TREE_BOTTOM, [420, 280, 30, 100], 0)
  
  #Draw leafs
  pygame.draw.rect(surface, LEAFS, [50, 240, 30, 40], 0)
  pygame.draw.rect(surface, LEAFS, [420, 240, 30, 40], 0)
  
  #Draw Home base
  pygame.draw.rect(surface, BASE, [105,120,290,260], 0)
  
  #Draw home top
  pygame.draw.polygon(surface, RED, [[75,120], [430,120], [245, 5]], 0)
  
  #Draw windows
  pygame.draw.rect(surface, BLACK, [155, 155, 30, 30], 0)
  pygame.draw.rect(surface, BLACK, [235, 155, 30, 30], 0)
  pygame.draw.rect(surface, BLACK, [315, 155, 30, 30], 0)
  
  pygame.draw.rect(surface, BLACK, [155, 215, 30, 30], 0)
  pygame.draw.rect(surface, BLACK, [235, 215, 30, 30], 0)
  pygame.draw.rect(surface, BLACK, [315, 215, 30, 30], 0)
  
  pygame.draw.rect(surface, BLACK, [155, 275, 30, 30], 0)
  pygame.draw.rect(surface, BLACK, [235, 275, 30, 30], 0)
  pygame.draw.rect(surface, BLACK, [315, 275, 30, 30], 0)
  
  #Draw door
  pygame.draw.rect(surface, WHITE, [190, 315, 30, 65], 0)
  pygame.draw.rect(surface, WHITE, [290, 315, 30, 65], 0)
  
  pygame.draw.rect(surface, BLACK, [200, 340, 20, 10], 0)
  pygame.draw.rect(surface, BLACK, [290, 340, 20, 10], 0)
  
  pygame.display.flip()
  clock.tick(5)
   
#Shutdown display module
pygame.display.quit()