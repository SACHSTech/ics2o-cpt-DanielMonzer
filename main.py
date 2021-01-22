""" 
A basic pygame template
"""
 
import pygame
import random

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
 
pygame.init()
  
# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)
 
background_image = pygame.image.load('space.jpg').convert()
player_image = pygame.image.load('player.png').convert()
player_image.set_colorkey(BLACK)
laser_image = pygame.image.load('laser.png').convert()
enemy_image = pygame.image.load('Virus.png').convert()
enemy_image.set_colorkey(WHITE)

background_position = [0, 0]

pygame.display.set_caption("Space Virus")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#enemy 1-6 properties
enemy1_x = random.randint(50, 750)
enemy1_y = random.randint(20, 250)
enemy2_x = random.randint(50, 750)
enemy2_y = random.randint(20, 250)
enemy3_x = random.randint(50, 750)
enemy3_y = random.randint(20, 250)
enemy4_x = random.randint(50, 750)
enemy4_y = random.randint(20, 250)
enemy5_x = random.randint(50, 750)
enemy5_y = random.randint(20, 250)
enemy6_x = random.randint(50, 750)
enemy6_y = random.randint(20, 250)
enemy_x_move = 4
enemy_y_move = 1

#player properties
player_x = 400
player_y = 400
player_y_move = 0
player_x_move = 0
Player_hit = False

#laser properties
laser_x = 5
laser_y = 10
laser_velocity = 0
fire = False
laser_hit = False

screen.blit(background_image, (0, 0))
# -------- Main Program Loop -----------
while not done:   
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
      
    screen.blit(background_image, (0, 0))
    
    # --- Game logic should go here
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_x_move = -5
        if event.key == pygame.K_RIGHT:
            player_x_move = 5
        if event.key == pygame.K_UP:
            player_y_move = -5
        if event.key == pygame.K_DOWN:
            player_y_move = 5
        if event.key == pygame.K_LSHIFT:
            if not fire:
                laser_x = player_x + 47
                laser_y = player_y -50
                fire = True
       
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            player_x_move = 0
            player_y_move = 0

    player_x += player_x_move
    if player_x <= 0:
        player_x = 0
    elif player_x >= 700:
        player_x = 700

    player_y += player_y_move
    if player_y <= 0:
        player_y = 0
    elif player_y >= 525:
        player_y = 525
        
    if fire:
        screen.blit(laser_image, (laser_x, laser_y))
        laser_velocity = -10
        laser_y -= 10
        if laser_y < 0:
            laser_velocity = 0
            fire = False
    #enemy movement
    enemy1_x += enemy_x_move
    if enemy1_x >= 800:
        enemy1_x = 0

    enemy1_y += enemy_y_move
    if enemy1_y >= 600:
        enemy1_y = 0
    
    enemy2_x += enemy_x_move
    if enemy2_x >= 800:
        enemy2_x = 0

    enemy2_y += enemy_y_move
    if enemy2_y >= 600:
        enemy2_y = 0

    enemy3_x += enemy_x_move
    if enemy3_x >= 800:
        enemy3_x = 0

    enemy3_y += enemy_y_move
    if enemy3_y >= 600:
        enemy3_y = 0    
    
    enemy4_x += enemy_x_move
    if enemy4_x >= 800:
        enemy4_x = 0

    enemy4_y += enemy_y_move
    if enemy4_y >= 600:
        enemy4_y = 0

    enemy5_x += enemy_x_move
    if enemy5_x >= 800:
        enemy5_x = 0

    enemy5_y += enemy_y_move
    if enemy5_y >= 600:
        enemy5_y = 0

    enemy6_x += enemy_x_move
    if enemy6_x >= 800:
        enemy6_x = 0
    
    enemy6_y += enemy_y_move
    if enemy6_y >= 600:
        enemy6_y = 0


    # --- Drawing code should go here
    screen.blit(enemy_image, (enemy1_x, enemy1_y))
    screen.blit(enemy_image, (enemy2_x, enemy2_y))
    screen.blit(enemy_image, (enemy3_x, enemy3_y))
    screen.blit(enemy_image, (enemy4_x, enemy4_y))
    screen.blit(enemy_image, (enemy5_x, enemy5_y))
    screen.blit(enemy_image, (enemy6_x, enemy6_y))
    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.
    
    screen.blit(player_image, (player_x, player_y))
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
