import pygame

SCREENWIDTH = 900
SCREENHEIGHT = 500
WHITE = (255,255,255)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #2. Set the window fill
        # window.fill(WHITE)
        #3. Update the window; without this the setting will not take effect
        # pygame.display.update()
    pygame.quit()

window = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
# 1.  set the caption for the window
# pygame.display.set_caption('My GWC Game')
main()