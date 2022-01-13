import pygame, sys, os

os.environ['SDL_VIDEO_CENTERED'] = '1'
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen size
width = 970
height = 520
fps = 60

class Paddle:
    def __init__(self, width, height, speed, xpos):
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pygame.Surface(self.width, self.height)
        self.rect = pygame.Rect(self.width * 2, height/2 - (self.height / 2), self.width, self.height)


def main():
    global width, height, WHITE
    pygame.init()

    # Paddle size
    p_width = 40
    p_height = 150
    p_speed = 1

    # Paddle 1
    p1_x = 40
    p1_y = height/2 - (p_height / 2)
    # p1_rect = pygame.Rect(p_width * 2, height/2 - (p_height / 2), p_width, p_height)
    p1_up = p1_down = False

    # Paddle 2
    p2_x = width - 2 * p_width
    p2_y = height/2 - (p_height / 2)
    # p2_rect = pygame.Rect(width - (p_width * 3), width / 2 - (p_width / 2), p_width, p_height)
    p2_up = p2_down = False

    pygame.display.set_caption("Pong")
    screen = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 50)

    # title variables
    title = font.render("Pong", 1, BLACK)
    titlepos = title.get_rect()
    titlepos.centerx = screen.get_rect().centerx

    # subtitle variables
    sub_title = font.render("Click Here to Start", 1, BLACK)
    sub_titlepos = sub_title.get_rect()
    sub_titlepos.center = screen.get_rect().center

    # paddle variables
    paddle1 = pygame.Surface((p_width, p_height)).convert()
    paddle1.fill(WHITE)
    paddle2 = pygame.Surface((p_width, p_height)).convert()
    paddle2.fill(WHITE)

    # ball variables
    ball_width = ball_height = 20
    ball = pygame.Surface((ball_width, ball_height)).convert()
    ball_rect = pygame.Rect(width/2 - (ball_width/2), height/2 - (ball_height/2), ball_width, ball_height)
    ball.fill(WHITE)
    ball_speed = [1, 1]

    beg_time = pygame.time.get_ticks()
    intro = True
    while intro:
        screen.fill(WHITE)
        screen.blit(title, titlepos)

        # Blinking Text
        cur_time = pygame.time.get_ticks()
        if ((cur_time - beg_time) % 1000) < 500:
            screen.blit(sub_title, sub_titlepos)

            # pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_RETURN] != 0:
                screen.blit(sub_title, sub_titlepos)
                pygame.display.flip()
                pygame.time.wait(1500)
                intro = False
        clock.tick(60)

    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # second player keys
                if event.key == pygame.K_w:
                    p1_up = True
                    p1_down = False
                elif event.key == pygame.K_s:
                    p1_up = False
                    p1_down = True
                if event.key == pygame.K_UP:
                    # remove p1 to make this a two players
                    p1_up = True
                    p1_down = False
                    # remove p1 to make this a two players
                    p2_up = True
                    p2_down = False
                elif event.key == pygame.K_DOWN:
                    # remove p1 to make this a two players
                    p1_up = False
                    p1_down = True
                    # remove p1 to make this a two players
                    p2_up = False
                    p2_down = True
            if event.type == pygame.KEYUP:
                p1_up = p2_up = p1_down = p2_down = False

        if p1_y < 0:
            p1_y = 0
        if p2_y < 0:
            p2_y = 0
        if p1_y > height - p_height:
            p1_y = height - p_height
        if p2_y > height - p_height:
            p2_y = height - p_height
        if p1_up:
            p1_y -= p_speed
        elif p1_down:
            p1_y += p_speed
        if p2_up:
            p2_y -= p_speed
        elif p2_down:
            p2_y += p_speed

        if p1_x + p_width - 5 < ball_rect.right < p1_x + p_width + 5:
            if ball_rect.top <= p1_y + 150 and ball_rect.bottom >= p1_y - 150:
                ball_speed[0] = -ball_speed[0]
        elif p2_x - 5 < ball_rect.right < p2_x + 5:
            if ball_rect.top <= p2_y + 150 and ball_rect.bottom >= p2_y - 150:
                ball_speed[0] = -ball_speed[0]
        elif ball_rect.right > p2_x + p_width:
            print ('Game Over - Person 1 wins')
            return False
        elif ball_rect.right < p1_x:
            print ('Game Over - Person 2 wins')
            return False
        elif ball_rect.top > height - ball_rect.height:
            ball_speed[1] = -ball_speed[1]
        elif ball_rect.top < 0:
            ball_speed[1] = -ball_speed[1]

        screen.fill(BLACK)
        ball_rect = ball_rect.move(ball_speed)
        screen.blit(ball, ball_rect)
        screen.blit(paddle1, (p1_x, p1_y))
        screen.blit(paddle2, (p2_x, p2_y))
        pygame.display.flip()


if __name__ == "__main__":
    main()
