import pygame
from random import randint
import os


pygame.mixer.init()


x = pygame.init()


#colour
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
# creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Bentlee")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)





def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])

def welcome():
    pygame.mixer.music.load("front.mp3")
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        front_img = pygame.image.load("front.jpg")
        front_img = pygame.transform.scale(front_img, (screen_width, screen_height)).convert_alpha()
        gameWindow.blit(front_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #pygame.mixer.music.load("bg.mp3")
                    #pygame.mixer.music.play()
                    gameloop()


        pygame.display.update()
        clock.tick(60)

#creating infinity loop
def gameloop():
    # game specific variables
    exit_game = False
    game_over = False

    snake_x = 55
    snake_y = 60

    velocity_x = 0
    velocity_y = 0

    food_x = randint(20, 890)
    food_y = randint(20, 590)
    score = 0
    init_velocity = 8

    snake_size = 10

    fps = 20

    snk_list = []
    snk_length = 1

    

    if(not os.path.exists("high_score.txt")):
        f = open("high_score.txt","w")
        f.write("0")
    f = open("high_score.txt", "r")
    high_score = f.read()

    while not exit_game:

        if game_over:
            gameWindow.fill(white)

            lst_img = pygame.image.load("last.jpg")
            lst_img = pygame.transform.scale(lst_img, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(lst_img,(0,0))

            text_screen(str(score), red, 570, 400)
            f = open("high_score.txt", "w")
            f.write(str(high_score))
            text_screen(str(high_score), red, 670, 500)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        #pygame.mixer.music.load("bg.mp3")
                        #pygame.mixer.music.play()
                        gameloop()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=10


                food_x = randint(55,890 )
                food_y = randint(55,590)
                snk_length +=3
                if score > int(high_score):
                    high_score = score

            gameWindow.fill(white)

            bg_img = pygame.image.load("bg_img.jpg")
            bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(bg_img, (0, 0))

            text_screen("Score: " + str(score), red, 0, 0)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play()
                game_over = True


            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play()
                game_over = True

        plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()