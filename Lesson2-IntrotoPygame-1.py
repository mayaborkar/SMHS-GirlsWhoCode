# 1. Import the pygame
# import pygame

# 2. Set Screen width/height and register the screen
# SCREENWIDTH = 900
# SCREENHEIGHT = 500

# 3. Initialize the window
# window = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

# 4.  Loop until you get the QUIT event
run = True
while run:
    # 5.  capture events of type Quit gracefully
    # for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()