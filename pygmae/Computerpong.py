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
pygame.display.set_caption("Pong")

# -- Exit game flag set to false
done = False








# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

y2_direction = 0

xspeed = 1
yspeed = 1

ball_width = 20
x_val = 150
y_val = 200
x_direction = xspeed
y_direction = yspeed

padd_length = 15
padd_width = 60
x_padd = 0
y_padd = 60

padd2_length = 15
padd2_width = 60
x2_padd = 620
y2_padd = 60

score = 10
points = 0

inc = 0.1

padd_direction = 0
# Select the font to use, size, bold, italics
font = pygame.font.SysFont('Calibri', 25, True, False)
 
# Render the text. "True" means anti-aliased text.
# Black is the color. The variable BLACK was defined
# above as a list of [0, 0, 0]
# Note: This line creates an image of the letters,
# but does not put it on the screen yet.
text = font.render("Lives: " + str(score), True, WHITE)
 
# Put the image of the text on the screen at 250x250
screen.blit(text, [250, 250])

### -- Game Loop
while not done:
# -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                 padd_direction = -1
            elif event.key == pygame.K_DOWN:
                padd_direction = 1
            #End if
        elif event.type == pygame.KEYUP:
            padd_direction = 0
        #End if    
    #nextevent

        
        
            #End If
        
        #End If
    
    
     #Next event
    # -- Game logic goes after this comment
    x_val = x_val + x_direction
    y_val = y_val + y_direction
    
    y_padd += padd_direction

    y2_padd

    

    text = font.render("Lives: " + str(score), True, WHITE)
    text2 = font.render("Points: " + str(points), True, WHITE)
    
    # ball bounce

    

    if y_val < 0 or y_val > 460:
        y_direction = y_direction * -1
    
    if x_val < -10:
        x_val = 310
        y_val = 230
        x_direction *=-1
        score-=1
        

    if x_val > 650:
        x_val = 310
        y_val = 230
        x_direction *=-1
        score-=1
        

    # paddle bounce
    toppad = y_padd
    botpad = y_padd + 60

    toppad2 = y2_padd
    botpad2 = y2_padd + 60

    if x_val <= 15 and y_val < botpad and y_val > toppad:
        x_direction = x_direction * -1
        y_direction = y_direction * -1
        points+=1
        
        if x_direction > 0:
            x_direction += inc
        else:
            x_direction -= inc
        if y_direction >0:    
            y_direction += inc
        else:
            y_direction -= inc
    
    if x_val >= 615 and y_val < botpad2 and y_val > toppad2:
        x_direction = x_direction * -1
        y_direction = y_direction * -1
        points+=1
        
        if x_direction > 0:
            x_direction += inc
        else:
            x_direction -= inc
        if y_direction >0:    
            y_direction += inc
        else:
            y_direction -= inc

    if score < 1:
        done = True
    
    ymid = y2_padd +30

    if ymid > y_val:
        y2_direction = -0.5
    elif ymid < y_val:
        y2_direction = 0.5

    y2_padd += y2_direction
    
    # -- Screen background is BLACK
    screen.fill (BLACK)
    
    # -- Draw here
    pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,ball_width))
    pygame.draw.rect(screen, WHITE,(x_padd,y_padd,padd_length,padd_width))
    screen.blit(text, [0, 0])
    
    pygame.draw.rect(screen, WHITE,(x2_padd,y2_padd,padd2_length,padd2_width))
    
    screen.blit(text2, [400, 400])
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
     # - The clock ticks over
    clock.tick(120)
    
#End While - End of game loop
pygame.quit()

