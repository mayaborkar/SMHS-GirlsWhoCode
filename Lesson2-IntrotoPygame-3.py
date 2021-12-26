import pygame
# 4. Import os
import os

SCREENWIDTH = 900
SCREENHEIGHT = 500
WHITE = (255,255,255)
# 1.  Define the screen refresh rate
FPS = 60
#5. Import Ship Image
SHIP1_IMAGE =  pygame.image.load("spaceship_red.png")
# 7. size the ship
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40
SHIP1 = pygame.transform.scale(SHIP1_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
# 8. rotate the ship
SHIP1 = pygame.transform.rotate (SHIP1, 90)
SHIP2 = pygame.transform.rotate (SHIP1, 180)

def main():
    run = True
    # 2. Initialize the clock
    clock = pygame.time.Clock()
    while run:
        # 3. Set the watch time on the clock
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)
        # 6. show the screen
        window.blit(SHIP1, (300,100))
        # 8. Show the next space ship
        window.blit(SHIP2, (700, 100))
        pygame.display.update()
    pygame.quit()

window = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption('My GWC Game')
main()