import pygame

# 1. Set Screen width/height and register the screen
# SCREENWIDTH = 900
# SCREENHEIGHT = 500

# 2.  write a for loop to ;
def main ():
    run = True
    while run :
        # run = True
        # 3.  capture events of type Quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

# window = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

main()