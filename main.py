""" 
A basic pygame template
"""
 
import pygame
import random
import time

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
enemy2_image = pygame.image.load('virus2.jpg').convert()
enemy2_image.set_colorkey(WHITE)
enemy3_image = pygame.image.load('virus3 (2).png').convert()
enemy3_image.set_colorkey(WHITE)
enemy4_image = pygame.image.load('virus4.png').convert()
enemy4_image.set_colorkey(WHITE)

background_position = [0, 0]

pygame.display.set_caption("Space Virus")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

level = 1

#enemy 1-6 properties
enemy1_x = random.randint(10, 700)
enemy1_y = random.randint(20, 250)
enemy2_x = random.randint(10, 700)
enemy2_y = random.randint(20, 250)
enemy3_x = random.randint(10, 700)
enemy3_y = random.randint(20, 250)
enemy4_x = random.randint(10, 700)
enemy4_y = random.randint(20, 250)
enemy5_x = random.randint(10, 700)
enemy5_y = random.randint(20, 250)
enemy6_x = random.randint(10, 700)
enemy6_y = random.randint(20, 250)
enemy1_x_move = 4
enemy2_x_move = 4
enemy3_x_move = 4
enemy4_x_move = 4
enemy5_x_move = 4
enemy6_x_move = 4
enemy_y_move = 1
alive1 = True
alive2 = True
alive3 = True
alive4 = True
alive5 = True
alive6 = True

#player properties
player_x = 400
player_y = 400
player_y_move = 0
player_x_move = 0
player_alive = True

#laser properties
laser_x = 5
laser_y = 10
laser_velocity = 0
fire = False

#Make the enemies move the same way
def reset_speed(speed):
    if speed < 0:
        return speed * -1
    else:
        return speed

#If one of the ships corners hits an enemy player dies
def player_hit(enemy_x, enemy_y, player_x, player_y):
    if player_x < enemy_x + 80 and player_x > enemy_x and player_y < enemy_y + 61 and player_y > enemy_y or player_x + 99 < enemy_x + 80 and player_x + 99 > enemy_x and player_y < enemy_y + 61 and player_y > enemy_y or player_x < enemy_x + 80 and player_x > enemy_x and player_y + 75 < enemy_y + 61 and player_y + 75 > enemy_y or player_x + 99 < enemy_x + 80 and player_x + 99 > enemy_x and player_y + 75 < enemy_y + 61 and player_y + 75 > enemy_y:
        return False
    return True

#Set count for enemies defeated
count = 0

#Blit level 1 and info of 1st virus
screen.blit(background_image, (0, 0))
font = pygame.font.SysFont('Calibri', 50, True, False)
text = font.render("Level 1", True, GREEN)
screen.blit(text, [325, 275])
pygame.display.update()
time.sleep(2)
screen.blit(background_image, (0, 0))
font = pygame.font.SysFont('Calibri', 25, True, False)
text = font.render("Adware is the least dangerous.", True, GREEN)
screen.blit(text, [235, 255])
font = pygame.font.SysFont('Calibri', 25, True, False)
text = font.render("It collects information from your browsing and sells it to ads.", True, GREEN)
screen.blit(text, [100, 275])
pygame.display.update()
time.sleep(4)

# -------- Main Program Loop -----------
while not done:   
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
      
    screen.blit(background_image, (0, 0))
    
    # --- Game logic should go here
    #Make key inputs to move
    if event.type == pygame.KEYDOWN and player_alive:
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
                laser_y = player_y -15
                fire = True
       
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            player_x_move = 0
            player_y_move = 0

    #Set player boundaries
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

    #Make bullet move     
    if fire:
        screen.blit(laser_image, (laser_x, laser_y))
        laser_velocity = -10
        laser_y -= 10
        if laser_y < 0:
            laser_velocity = 0
            fire = False
    
    #Blit level 2 + info and spawn enemies with increased speed
    if count == 6 and player_alive and level == 1:
        font = pygame.font.SysFont('Calibri', 50, True, False)
        text = font.render("Level 2", True, GREEN)
        screen.blit(text, [325, 275])
        pygame.display.update()
        time.sleep(2)
        screen.blit(background_image, (0, 0))
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Spyware is a type of malware installed without knowledge.", True, GREEN)
        screen.blit(text, [95, 255])
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("It invades the device, steals sensitive information and internet usage data.", True, GREEN)
        screen.blit(text, [20, 275])
        player_x = 348
        player_y = 400
        enemy1_x = random.randint(10, 700)
        enemy1_y = random.randint(20, 250)
        enemy2_x = random.randint(10, 700)
        enemy2_y = random.randint(20, 250)
        enemy3_x = random.randint(10, 700)
        enemy3_y = random.randint(20, 250)
        enemy4_x = random.randint(10, 700)
        enemy4_y = random.randint(20, 250)
        enemy5_x = random.randint(10, 700)
        enemy5_y = random.randint(20, 250)
        enemy6_x = random.randint(10, 700)
        enemy6_y = random.randint(20, 250)
        enemy1_x_move = reset_speed(enemy1_x_move)
        enemy2_x_move = reset_speed(enemy2_x_move)
        enemy3_x_move = reset_speed(enemy3_x_move)
        enemy4_x_move = reset_speed(enemy4_x_move)
        enemy5_x_move = reset_speed(enemy5_x_move)
        enemy6_x_move = reset_speed(enemy6_x_move)
        enemy1_x_move += 1
        enemy2_x_move += 1
        enemy3_x_move += 1
        enemy4_x_move += 1
        enemy5_x_move += 1
        enemy6_x_move += 1 
        enemy_y_move += 0.2
        alive1 = True
        alive2 = True
        alive3 = True
        alive4 = True
        alive5 = True
        alive6 = True
        level = 2
        pygame.display.update()
        time.sleep(5)

    #Blit level 3 + info and spawn enemies with increased speed
    if count == 12 and player_alive and level == 2:
        font = pygame.font.SysFont('Calibri', 50, True, False)
        text = font.render("Level 3", True, GREEN)
        screen.blit(text, [325, 275])
        pygame.display.update()
        time.sleep(2)
        screen.blit(background_image, (0, 0))
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Rootkit is designed to be hard to detect and remove.", True, GREEN)
        screen.blit(text, [120, 255])
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("It accesses the owner’s information without the owner knowing.", True, GREEN)
        screen.blit(text, [65, 275])
        player_x = 348
        player_y = 400
        enemy1_x = random.randint(10, 700)
        enemy1_y = random.randint(20, 250)
        enemy2_x = random.randint(10, 700)
        enemy2_y = random.randint(20, 250)
        enemy3_x = random.randint(10, 700)
        enemy3_y = random.randint(20, 250)
        enemy4_x = random.randint(10, 700)
        enemy4_y = random.randint(20, 250)
        enemy5_x = random.randint(10, 700)
        enemy5_y = random.randint(20, 250)
        enemy6_x = random.randint(10, 700)
        enemy6_y = random.randint(20, 250)
        enemy1_x_move = reset_speed(enemy1_x_move)
        enemy2_x_move = reset_speed(enemy2_x_move)
        enemy3_x_move = reset_speed(enemy3_x_move)
        enemy4_x_move = reset_speed(enemy4_x_move)
        enemy5_x_move = reset_speed(enemy5_x_move)
        enemy6_x_move = reset_speed(enemy6_x_move)
        enemy1_x_move += 1
        enemy2_x_move += 1
        enemy3_x_move += 1
        enemy4_x_move += 1
        enemy5_x_move += 1
        enemy6_x_move += 1 
        enemy_y_move += 0.2
        alive1 = True
        alive2 = True
        alive3 = True
        alive4 = True
        alive5 = True
        alive6 = True
        level = 3
        pygame.display.update()
        time.sleep(5)

    #Blit level 4 + info and spawn enemies with increased speed and moving up
    if count == 18 and player_alive and level == 3:
        font = pygame.font.SysFont('Calibri', 50, True, False)
        text = font.render("Level 4", True, GREEN)
        screen.blit(text, [325, 275])
        pygame.display.update()
        time.sleep(2)
        screen.blit(background_image, (0, 0))
        font = pygame.font.SysFont('Calibri', 30, True, False)
        text = font.render("Trojan is the most dangerous Malware.", True, GREEN)
        screen.blit(text, [175, 250])
        font = pygame.font.SysFont('Calibri', 30, True, False)
        text = font.render("It discovers your financial information,", True, GREEN)
        screen.blit(text, [175, 275])
        font = pygame.font.SysFont('Calibri', 30, True, False)
        text = font.render("and takes over your computer’s system.", True, GREEN)
        screen.blit(text, [175, 300])
        player_x = 348
        player_y = 400
        enemy1_x = random.randint(10, 700)
        enemy1_y = random.randint(20, 250)
        enemy2_x = random.randint(10, 700)
        enemy2_y = random.randint(20, 250)
        enemy3_x = random.randint(10, 700)
        enemy3_y = random.randint(20, 250)
        enemy4_x = random.randint(10, 700)
        enemy4_y = random.randint(20, 250)
        enemy5_x = random.randint(10, 700)
        enemy5_y = random.randint(20, 250)
        enemy6_x = random.randint(10, 700)
        enemy6_y = random.randint(20, 250)
        enemy1_x_move = reset_speed(enemy1_x_move)
        enemy2_x_move = reset_speed(enemy2_x_move)
        enemy3_x_move = reset_speed(enemy3_x_move)
        enemy4_x_move = reset_speed(enemy4_x_move)
        enemy5_x_move = reset_speed(enemy5_x_move)
        enemy6_x_move = reset_speed(enemy6_x_move)
        enemy1_x_move += 1
        enemy2_x_move += 1
        enemy3_x_move += 1
        enemy4_x_move += 1
        enemy5_x_move += 1
        enemy6_x_move += 1 
        enemy_y_move += -2.8
        alive1 = True
        alive2 = True
        alive3 = True
        alive4 = True
        alive5 = True
        alive6 = True
        level = 4
        pygame.display.update()
        time.sleep(6)
    
    #Blit victory screen
    if count == 24 and player_alive and level == 4:
        font = pygame.font.SysFont('Calibri', 50, True, False)
        text = font.render("You killed the virus", True, GREEN)
        screen.blit(text, [205, 275])
    
    #Once player dies enemies die and defeat screen
    if not player_alive:
        alive1 = False
        alive2 = False
        alive3 = False
        alive4 = False
        alive5 = False
        alive6 = False
        font = pygame.font.SysFont('Calibri', 50, True, False)
        text = font.render("You couldn't kill the virus", True, RED)
        screen.blit(text, [150, 275])

    #Call to def player_hit while player alive
    if player_alive and alive1:
        player_alive = player_hit(enemy1_x, enemy1_y, player_x, player_y)
        
    if player_alive and alive2:
        player_alive = player_hit(enemy2_x, enemy2_y, player_x, player_y)

    if player_alive and alive3:
        player_alive = player_hit(enemy3_x, enemy3_y, player_x, player_y)

    if player_alive and alive4:
        player_alive = player_hit(enemy4_x, enemy4_y, player_x, player_y)

    if player_alive and alive5:
        player_alive = player_hit(enemy5_x, enemy5_y, player_x, player_y)

    if player_alive and alive6:
        player_alive = player_hit(enemy6_x, enemy6_y, player_x, player_y)

    #Make laser collision with enemies
    if laser_x < enemy1_x + 80 and laser_x > enemy1_x and laser_y < enemy1_y + 61 and laser_y > enemy1_y and alive1 and fire:
        alive1 = False
        fire = False
        count += 1
    
    if laser_x < enemy2_x + 80 and laser_x > enemy2_x and laser_y < enemy2_y + 61 and laser_y > enemy2_y and alive2 and fire:
        alive2 = False
        fire = False
        count += 1
    
    if laser_x < enemy3_x + 80 and laser_x > enemy3_x and laser_y < enemy3_y + 61 and laser_y > enemy3_y and alive3 and fire:
        alive3 = False
        fire = False
        count += 1

    if laser_x < enemy4_x + 80 and laser_x > enemy4_x and laser_y < enemy4_y + 61 and laser_y > enemy4_y and alive4 and fire:
        alive4 = False
        fire = False
        count += 1

    if laser_x < enemy5_x + 80 and laser_x > enemy5_x and laser_y < enemy5_y + 61 and laser_y > enemy5_y and alive5 and fire:
        alive5 = False
        fire = False
        count += 1
    
    if laser_x < enemy6_x + 80 and laser_x > enemy6_x and laser_y < enemy6_y + 61 and laser_y > enemy6_y and alive6 and fire:
        alive6 = False
        fire = False
        count += 1

    #Enemy movement + different enemies
    if alive1:
        if enemy1_x + 80 >= 800 or enemy1_x <= 0:
            enemy1_x_move *= -1
        enemy1_x += enemy1_x_move

        enemy1_y += enemy_y_move
        if enemy1_y >= 600:
            enemy1_y = 0
        if enemy1_y < 0:
            enemy1_y = 599
        
        if count < 6:
            screen.blit(enemy_image, (enemy1_x, enemy1_y))
        if count >= 6 and count < 12:
            screen.blit(enemy2_image, (enemy1_x, enemy1_y))
        if count >= 12 and count < 18:
            screen.blit(enemy3_image, (enemy1_x, enemy1_y))
        if count >= 18 and count < 24:
            screen.blit(enemy4_image, (enemy1_x, enemy1_y))

    if alive2:
        if enemy2_x + 80 >= 800 or enemy2_x <= 0:
            enemy2_x_move *= -1
        enemy2_x += enemy2_x_move

        enemy2_y += enemy_y_move
        if enemy2_y >= 600:
            enemy2_y = 0
        if enemy2_y < 0:
            enemy2_y = 599
        
        if count < 6:
            screen.blit(enemy_image, (enemy2_x, enemy2_y))
        if count >= 6 and count < 12:
            screen.blit(enemy2_image, (enemy2_x, enemy2_y))
        if count >= 12 and count < 18:
            screen.blit(enemy3_image, (enemy2_x, enemy2_y))
        if count >= 18 and count < 24:
            screen.blit(enemy4_image, (enemy2_x, enemy2_y))

    if alive3:
        if enemy3_x + 80 >= 800 or enemy3_x <= 0:
            enemy3_x_move *= -1
        enemy3_x += enemy3_x_move

        enemy3_y += enemy_y_move
        if enemy3_y >= 600:
            enemy3_y = 0
        if enemy3_y < 0:
            enemy3_y = 599
        
        if count < 6:
            screen.blit(enemy_image, (enemy3_x, enemy3_y))
        if count >= 6 and count < 12:
            screen.blit(enemy2_image, (enemy3_x, enemy3_y))
        if count >= 12 and count < 18:
            screen.blit(enemy3_image, (enemy3_x, enemy3_y))
        if count >= 18 and count < 24:
            screen.blit(enemy4_image, (enemy3_x, enemy3_y))   

    if alive4:
        if enemy4_x + 80 >= 800 or enemy4_x <= 0:
            enemy4_x_move *= -1
        enemy4_x += enemy4_x_move

        enemy4_y += enemy_y_move
        if enemy4_y >= 600:
            enemy4_y = 0
        if enemy4_y < 0:
            enemy4_y = 599
        
        if count < 6:
            screen.blit(enemy_image, (enemy4_x, enemy4_y))
        if count >= 6 and count < 12:
            screen.blit(enemy2_image, (enemy4_x, enemy4_y))
        if count >= 12 and count < 18:
            screen.blit(enemy3_image, (enemy4_x, enemy4_y))
        if count >= 18 and count < 24:
            screen.blit(enemy4_image, (enemy4_x, enemy4_y))

    if alive5:
        if enemy5_x + 80 >= 800 or enemy5_x <= 0:
            enemy5_x_move *= -1
        enemy5_x += enemy5_x_move

        enemy5_y += enemy_y_move
        if enemy5_y >= 600:
            enemy5_y = 0
        if enemy5_y < 0:
            enemy5_y = 599
        
        if count < 6:
            screen.blit(enemy_image, (enemy5_x, enemy5_y))
        if count >= 6 and count < 12:
            screen.blit(enemy2_image, (enemy5_x, enemy5_y))
        if count >= 12 and count < 18:
            screen.blit(enemy3_image, (enemy5_x, enemy5_y))
        if count >= 18 and count < 24:
            screen.blit(enemy4_image, (enemy5_x, enemy5_y))
    
    if alive6:
        if enemy6_x + 80 >= 800 or enemy6_x <= 0:
            enemy6_x_move *= -1
        enemy6_x += enemy6_x_move

        enemy6_y += enemy_y_move
        if enemy6_y >= 600:
            enemy6_y = 0
        if enemy6_y < 0:
            enemy6_y = 599
        
        if count < 6:
            screen.blit(enemy_image, (enemy6_x, enemy6_y))
        if count >= 6 and count < 12:
            screen.blit(enemy2_image, (enemy6_x, enemy6_y))
        if count >= 12 and count < 18:
            screen.blit(enemy3_image, (enemy6_x, enemy6_y))
        if count >= 18 and count < 24:
            screen.blit(enemy4_image, (enemy6_x, enemy6_y))

    #Show player while alive
    if player_alive:
        screen.blit(player_image, (player_x, player_y))
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
