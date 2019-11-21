import pygame
import random
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
BROWN = (100,100,0)

#sprites
class Snow(pygame.sprite.Sprite):

    def __init__ (self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        


    def update(self):
        #called each frame

        #moves block down pixel

        self.rect.y +=1
        if self.rect.y > screen_height:
            self.rect.y = random.randrange(-670, 0)
            self.rect.x = random.randrange(0, screen_width)

        

# -- Initialise PyGame
pygame.init()


block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()




for i in range (1000):
    aSnow = Snow(WHITE,1,1)
    block_list.add(aSnow)
    all_sprites_list.add(aSnow)
# -- Blank Screen
screen_height = 640
screen_width = 600
size = (screen_height,screen_width)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Snow")
# -- Exit game flag set to false
done = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
### -- Game Loop
while not done:
# -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
     #Next event
    # -- Game logic goes after this comment
    
    block_list.update()
    
    # -- Screen background is BLACK
    screen.fill (BLACK)
    
    # -- Draw here
    all_sprites_list.draw(screen)
    
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
     # - The clock ticks over
    clock.tick(60)
    
#End While - End of game loop
pygame.quit()

