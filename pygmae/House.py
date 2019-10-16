import pygame
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
BROWN = (100,100,0)

# -- Initialise PyGame
pygame.init()


# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My Window")

# -- Exit game flag set to false
done = False

sun_x = 40

sun_y = 40

x = 1






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

    sun_x = sun_x +20
    sun_y = sun_y + 1

    x = x + 1

    

    if sun_x > 1000:
        sun_x = 40

    if sun_y > 1000:
        sun_y = 0

    if x > 1000:
        x = -400
    # -- Screen background is BLACK
    screen.fill (BLACK)
    
    # -- Draw here
    pygame.draw.rect(screen, BLUE, (x+220,165,200,150))
    pygame.draw.rect(screen, WHITE, (x+240,200,20,20))
    pygame.draw.rect(screen, WHITE, (x+380,200,20,20))
    pygame.draw.rect(screen, WHITE, (x+240,250,20,20))
    pygame.draw.rect(screen, WHITE, (x+380,250,20,20))
    pygame.draw.rect(screen, BROWN, (x+310,250,20,65))
    pygame.draw.circle(screen, YELLOW, (sun_x,sun_y),40,0)
    
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
     # - The clock ticks over
    clock.tick(999999)
    
#End While - End of game loop
pygame.quit()

