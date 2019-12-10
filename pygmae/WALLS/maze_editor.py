import pygame
import json
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
BROWN = (100,100,0)

class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
        width = 10
        height = 10
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

# -- Initialise PyGame
pygame.init()



all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

# -- Blank Screen
size = (500,500)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My Window")

# -- Exit game flag set to false
done = False


file = open("NEWMAZE.JSON","r")



the = json.load(file)
last_pressed = []
print(the)

file.close()

for i in range (len(the)):
    for j in range (len(the[i])):
        if the[i][j] == 1:
            newwall = Wall(j*10,i*10)
            wall_list.add(newwall)
            all_sprite_list.add(newwall)




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



    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        print("Space")

        x = pos[0]//10
        y = pos[1]//10


        if [x,y] != last_pressed:
            if  the[y][x] == 1:
                the[y][x] = 0
                print("1 to 0")
                for wall in wall_list:
                    if wall.rect.collidepoint(pos):
                        wall.kill()
            elif the[y][x] == 0:
                the[y][x] = 1
                print("0 to 1")


            last_pressed = [x,y]




                
    # -- Game logic goes after this comment

    pos = pygame.mouse.get_pos()
    
    
    for i in range (len(the)):
        for j in range (len(the[i])):
            if the[i][j] == 1:
                newwall = Wall(j*10,i*10)
                wall_list.add(newwall)
                all_sprite_list.add(newwall)    
    









    # -- Screen background is BLACK

    all_sprite_list.update()
    screen.fill (BLACK)
    all_sprite_list.draw(screen)
    # -- Draw here

    all_sprite_list.update()
    
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
     # - The clock ticks over
    clock.tick(60)
    
#End While - End of game loop
pygame.quit()

