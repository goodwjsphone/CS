import pygame
import random
import time
import threading
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# --- Classes
direction = 0
difficulty = 3
damage = 0
maxdamage = 3
 
 
class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color,x,y):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        
        self.image = pygame.image.load("Invader.jpg").convert()
        self.image = pygame.transform.smoothscale(self.image, (25,20))
        self.image.set_colorkey(BLACK)
 
        self.rect = self.image.get_rect()
        self.rect.y = y * -1
        self.rect.x = x

    def BlockMove(self,speed):
        self.rect.y += speed
        if self.rect.y > 700:
            self.rect.y -= random.randrange(700,800)
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image = pygame.transform.smoothscale(self.image, (50,40))
        self.image.set_colorkey(BLACK)
        
        
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Update the player's position. """
 
        # move the player using up down keys

        
        

    def move(self,direction):
        if direction == "left":
            self.rect.x -= 1
        if direction =="right":
            self.rect.x += 1
    
        
    
 
 
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        
        self.image = pygame.image.load("Bullet.png").convert()
        self.image = pygame.transform.smoothscale(self.image, (2,4))
        self.image.set_colorkey(BLACK)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3

    
    
 
 
# --- Create the window
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
direction = 0
 
# --- Sprite lists
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()
 
# --- Create the sprites
 
for i in range(10):
    # This represents a block
    block = Block(BLUE,random.randrange(screen_width),random.randrange(800))
 
    
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = Player()
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
player.rect.y = 370

bigtick = 0
speed = 1
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x + 25
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.move('right')
    elif keys[pygame.K_LEFT]:
        player.move('left')
    

    # keys
    for block in block_list:
        block.BlockMove(1)
    
 
    # --- Game logic
    
    
    bigtick += 1
    if bigtick == 60:
        for i in range(10):
            # This represents a block
            block = Block(BLUE,random.randrange(screen_width),random.randrange(800))
     
        
     
            # Add the block to the list of objects
            block_list.add(block)
            all_sprites_list.add(block)
        
        speed+=1

        bigtick -= 60
        print ("yes")
    
 
    # Call the update() method on all the sprites
    all_sprites_list.update()
 
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            for i in range(difficulty):
                block = Block(BLUE,random.randrange(screen_width),random.randrange(800))
                block_list.add(block)
                all_sprites_list.add(block)
            print(score)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
    if pygame.sprite.spritecollide(player, block_list,True):
        print ("ohyeah")
        damage +=1
        if damage > maxdamage:
            done = True
    
    # --- Draw a frame
 
    # Clear the screen
    screen.fill(BLACK)
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)
 
pygame.quit()
