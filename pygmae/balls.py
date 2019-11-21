#Import libaries
import pygame
import math
import random
# Difine colours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (0,0,0)
#initialise pygame
pygame.init()
# set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width,screen_height])
#used to manage how fast the screen updates
clock = pygame.time.Clock()

# dfine the class ball
class Ball():
    #contsutcot function to define inital state of a ball object
    def __init__(self,x,y,col,x_speed,y_speed):
        #---class attributes---
        #ball position
        self.x = x
        self.y = y

        # ball vecotr
        self.change_x = x_speed
        self.change_y = y_speed

        #Ball colour
        self.color = col

        #Ball size
        self.size = 5


    # --- Class Methods ---
    # Dfines the balls movement
    def move(self):
            self.x += self.change_x
            self.y += self.change_y
            if self.x <0 + self.size or self.x > 700 - self.size:
                self.change_x *= -1
            if self.y <0 + self.size or self.y > 400 - self.size:
                self.change_y *= -1

    # Draws the ball on the screen
    
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,[self.x,self.y],self.size)

# set game loop ot false so it runs
done = False

#create an object using the ball class

theBall = Ball(100,100,RED,2,1)
theBall2 = Ball(50,100,RED,2,1)
my_balls = []
for i in range (1000):
        theBallx = Ball(random.randint(0,399),random.randint(0,699),RED,2,1)
        my_balls.append(theBallx)


#game loop
while not done:

    #clear the screen
    screen.fill(WHITE)

    #Draw the ball on the screen and then move it on
    theBall.draw(screen)
    theBall.move()
    theBall2.draw(screen)
    theBall2.move()

    for b in my_balls:
        b.draw(screen)
        b.move()

    

    

    # frame speed
    clock.tick(999)
    # update the screen with drawing
    pygame.display.flip()


pygame.quit
        
