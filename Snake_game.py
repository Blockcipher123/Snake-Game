import pygame
import random
import os


pygame.mixer.init()
pygame.init()




# colors
white = (255, 255,255)
red = (255, 0, 0)
black = (0,0, 0)
green = (9, 237, 24)


screen_width = 900
screen_hight = 600
# Creation Window
gameWindow = pygame.display.set_mode((screen_width, screen_hight))  

# Background Image
bgimg = pygame.image.load("back2.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_hight)).convert_alpha() 

# game over image
gameing = pygame.image.load("firstintro.png")
gameing = pygame.transform.scale(gameing, (screen_width, screen_hight)).convert_alpha()


# Game title
pygame.display.set_caption('Snakes_Game')
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    # print(snk_list)
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x, y, snake_size, snake_size])



def welcome():
    exit_game =  False
    while not exit_game:
        gameWindow.fill((220,100,229))
        text_screen("Welcome To Snake", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 230, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("back.mp3")
                    pygame.mixer.music.play()
                    gameloop()




        pygame.display.update()
        clock.tick(50)    




# Game loop
def gameloop():

    # Game specific variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    # check if highscore file exists
    if (not os.path.exists("")):
        with open("hiscore.txt", "w") as f:
            f.write("0")


    with open("highscore.txt", 'r') as f:
        highscore = f.read()

    apple_x = random.randint(20,screen_width/2)
    apple_y = random.randint(20,screen_hight/2)

    score = 0
    init_velocity = 5

    snake_size = 30
    fps = 50
         
    while not exit_game:

        if game_over:
            with open("highscore.txt", 'w') as f:
                f.write(str(highscore))
            gameWindow.fill((0,0,0))
            gameWindow.blit(gameing,(5,5))
            text_screen(f"Your Score is {score}", red, 320, 400)



            # foont = text_screen(f'By Block_Cipher', green, 500, 500)
            # foont1(Font(20))

            # if score > highscore:
            #     text_screen(f"Great, Score is {score}", red, 320, 400)
            

            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # gameloop()
                        welcome() 


        else:


            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
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


                    # if event.click == pygame.C_RIGHT:
                    #     velocity_x = init_velocity
                    #     velocity_y = 0

                    if event.key == pygame.K_q:
                        score += 10       

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y 

            if abs (snake_x - apple_x) <15 and abs(snake_y - apple_y) <15:
                score += 10

                apple_x = random.randint(20,screen_width/2)
                apple_y = random.randint(20,screen_hight/2)
                snk_length += 5
                # print(highscore)
                if score>int(highscore):
                    highscore = score


            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0,0))
            text_screen("Score : " + str(score) + "  Hiscore : " + str(highscore), green, 5 , 5 )
            pygame.draw.rect(gameWindow, red, [apple_x, apple_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_length: 
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()


            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_hight:
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                # print("Game over ! -")

            # pygame.draw.rect(gameWindow,black,[snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
welcome()   


